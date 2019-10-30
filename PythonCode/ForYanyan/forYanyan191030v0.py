# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:20:29 2019
for 李航 统计书 第十一章 习题
"""
import numpy as np
M1 = np.array([[  0,   0],
               [0.5, 0.5]])
M2 = np.array([[0.3, 0.7],
               [0.7, 0.3]])
M3 = np.array([[0.5, 0.5],
               [0.6, 0.4]])

def get_probility(i, j, k):
    return M1[1, i] * M2[i, j] * M3[j, k] # 计算路径 i-j-k 的 概率

route = [] # route 存储所有可能路径
ps = [] # 存储所有 概率值

for i in range(2):
    for j in range(2):
        for k in range(2):
            p = get_probility(i, j, k) 
            route.append('{}-{}-{}'.format(i+1, j+1, k+1)) # 装载数值
            ps.append(p) # 装载数值
            print("路径{}-{}-{}: P = {:f}".format(i+1, j+1, k+1, p))
print("max probility: %f" % max(ps))
print("max 路径",route[ps.index(max(ps))])