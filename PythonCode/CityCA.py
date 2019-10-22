#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import numpy as np
import gdal
import os
 
URBAN = 1
THRESHOLDTOURBAN = 0.2  # 转化阈值，高于变城市用地
THRESHOLDTOUNURBAN = 0.4  # 转化阈值，高于变非城市用地
INTERVAL = 100  # 划分“至道路的距离”的区间长度
SELFTOURBAN = [0., 1.0, 0.5, 0.3, 0.8, 0.]  # 本身开发适宜性
 
 
class LandWorld:
    width = 100
    height = 100
 
    def __init__(self, firstImage, secondImage, distanceToRoad):
        try:
            dataset1 = gdal.Open(firstImage)
            dataset2 = gdal.Open(secondImage)
            datasetRoad = gdal.Open(distanceToRoad)
            self.geotransform = dataset1.GetGeoTransform()  # 存储坐标转换信息
            self.projection = dataset1.GetProjection()  # 存储坐标信息
            # 第一幅图像定义元胞空间
            self.cells = dataset1.ReadAsArray()
            self.width = dataset1.RasterXSize
            self.height = dataset1.RasterYSize
 
            # 第二幅图定义邻域情景，计算邻域影响下的转化概率
            self.image2 = dataset2.ReadAsArray()
 
            # 至道路的距离是决定是否向城市用地转化的条件之一
            self.distance = datasetRoad.ReadAsArray()
 
        except:
            print("数据读取出错！")
 
    def GetWidth(self):
        return self.width
 
    def GetHeight(self):
        return self.height
 
    def TryGetCell(self, h, w):
        return self.cells[min(h, self.height - 1)][min(w, self.width - 1)]  # 注意边缘处理
 
    def GetNearbyUrbanCount(self, h, w):
        """
        统计邻域城市用地数量
        """
        nearby = [self.TryGetCell(h + dy, w + dx) for dx in [-1, 0, 1]
                  for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
        return len(list(filter(lambda x: x == URBAN, nearby)))
 
    def FindDistanceLaw(self):
        """
        获取城市用地与distance to road的关系
        返回每个距离区间的权重
        问题：如何区间间隔定义为interval
        """
        # global interval
        bin = np.zeros(int(np.max(self.distance) // INTERVAL + 1), dtype=np.int)
        for i in range(self.height):
            for j in range(self.width):
                if self.distance[i, j] >= 0:
                    bin[int(self.distance[i, j] // INTERVAL)] += 1
        max = np.max(bin) * 1.0
        WBin = bin / max
        return WBin
 
    def GetDistanceWeights(self):
        """
        获取道路因素影响下的城市化权重
        """
        WDistance = np.zeros([self.height, self.width])
        WBin = self.FindDistanceLaw()
 
        for i in range(self.height):
            for j in range(self.width):
                WDistance[i, j] = WBin[int(self.distance[i, j] // 100)]
        return WDistance
 
    def FindNeighborLawToUnurban(self):
        """
         两期土地利用数据统计城市用地到非城市用地转变的邻域规律
         返回各邻域情景下（城市->非城市）的比例
         """
        scenes = np.zeros(9, dtype=np.int)  # 下标代表邻域城市用地数量
        tounurban = np.zeros(9, dtype=np.int)
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i, j] == URBAN:
                    n = int(self.GetNearbyUrbanCount(i, j))
                    scenes[n] += 1
                    if not (self.image2[i, j] == URBAN):
                        tounurban[n] += 1
        return tounurban / (scenes + 0.0001)
 
    def FindNeighborLawToUrban(self):
        """
         两期土地利用数据统计非城市用地到城市用地转变的邻域规律
         返回各邻域情景下（非城市->城市）的比例
         """
        scenes = np.zeros(9, dtype=np.int)  # 下标代表邻域城市用地数量
        tourban = np.zeros(9, dtype=np.int)
        for i in range(self.height):
            for j in range(self.width):
                if not (self.cells[i, j] == URBAN) and not (self.cells[i, j] == 0):
                    n = int(self.GetNearbyUrbanCount(i, j))
                    scenes[n] += 1
                    if self.image2[i, j] == URBAN:
                        tourban[n] += 1
        return tourban / (scenes + 0.0001)  # 防止分母为零
 
    def GetNeighborWeight(self):
        """
        获取邻域影响权重
        返回每一个元胞单元的邻域权重
        城市单元（->非城市权重），非城市单元（->城市权重）
        """
        WNeighbor = np.zeros([self.height, self.width])
        urban = self.FindNeighborLawToUrban()  # 获取邻域情景对应的转化概率
        unurban = self.FindNeighborLawToUnurban()
 
        for i in range(self.height):
            for j in range(self.width):
 
                # 如果是城市元胞，统计变成非城市用地的概率
                if self.cells[i, j] == URBAN:
                    n = self.GetNearbyUrbanCount(i, j)
                    WNeighbor[i, j] = unurban[int(n)]
 
                # 如果是非城市元胞，统计变成城市用地的概率
                elif not (self.cells[i, j] == 0):
                    n = self.GetNearbyUrbanCount(i, j)
                    WNeighbor[i, j] = urban[int(n)]
        return WNeighbor
 
    def Update(self):
        """
        更新元胞
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i, j] == URBAN:
                    # 城市用地：是否变成非城市用地(统一变成草地4)
                    score1 = (1 - self.roadscore[i, j]) * self.neighborscore[i, j]
                    if score1 > THRESHOLDTOUNURBAN:
                        self.cells[i, j] = 4
 
                elif not (self.cells[i, j] == 0):
                    # 城市用地：是否变成非城市用地
                    score2 = self.roadscore[i, j] * self.neighborscore[i, j]
                    if score2 > THRESHOLDTOURBAN:
                        self.cells[i, j] = 1
 
    def Start(self, N):
        """
        CA开始，自动迭代
        """
        self.roadscore = self.GetDistanceWeights()
        self.neighborscore = self.GetNeighborWeight()
        for i in range(N):
            self.Update()
 
    def CreateImage(self, filename):
        """
        根据元胞生成图像
        """
        # driver = gdal.GetDriverByName("GTiff")
        # tods = driver.Create(filename, self.width, self.height, 1, options=["INTERLEAVE=PIXEL"])
        # tods.WriteRaster(0, 0, self.width, self.height, self.cells.tostring(), self.width, self.height)
 
        # 怎么导入空间参考系统？
        driver = gdal.GetDriverByName("GTiff")
        tods = driver.Create(filename, self.width, self.height, 1, options=["INTERLEAVE=PIXEL"])
        tods.SetGeoTransform(self.geotransform)
        tods.SetProjection(self.projection)
        tods.WriteRaster(0, 0, self.width, self.height, self.cells.tostring(), self.width, self.height)
 
 
if __name__ == "__main__":
    os.chdir('F:/CA/cityCA/data/')
    world = LandWorld('gc00.tif', 'gc05.tif', 'DisToTownRoad.tif')
    N = 3
    world.Start(N)
    world.CreateImage('F:/CA/cityCA/中间成果/运行输出/' + 'result' + str(N) + '.tif')
    '''
--------------------- 
作者：weixin_34153893 
来源：CSDN 
原文：https://blog.csdn.net/weixin_34153893/article/details/88251040 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
