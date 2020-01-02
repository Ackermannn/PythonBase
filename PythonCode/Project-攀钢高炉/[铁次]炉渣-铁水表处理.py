# -*- coding: utf-8 -*-
"""
同一铁次分多个罐号 取值平均

还未处理异常值, 缺失值
"""
import pandas as pd
import numpy as np


def iron_order(path_r, path_s):
    '''
    path_r: 读取的路径
    path_s: 保存的路径
    对带有铁次号的表的数据规整.即, index 为铁次号 与 日期, column'采集项名称','采集项编码'
    
    '''
    df = pd.read_excel(path_r)
    df = df.pivot_table(index=['铁次号','业务处理时间'], # 猜测铁次号第一位数字代表样本号
              columns=['采集项名称','采集项编码'], values='采集项值',
              aggfunc = np.mean)
    df.to_excel(path_s)
    
if __name__ == '__main__':
    
    path_r = [r'./origin/炉渣成分表.xlsx',
              r'./origin/铁水成分表.xlsx',
              r'./origin/铁水实绩表.xlsx',
              r'./origin/铁水质量表.xlsx']
    
    path_s = [r'./report/new铁水成分表.xlsx',
              r'./report/new铁水实绩表.xlsx',
              r'./report/new铁水质量表.xlsx',
              r'./report/new炉渣成分表.xlsx']
    
    for i in range(len(path_r)):
        iron_order(path_r[i],path_s[i])
        
#如果要对四个表进行合并:
#out = pd.merge(df1, df2, left_index=True, right_index=True,how='outer')