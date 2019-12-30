# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:43:36 2019

@author: Ackerman
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
'''
# 乘以一个常数并不影响 相关系数! 

# 计算鼓风动能 与 铁水硅含量的时间滞后分析

# 鼓风动能 = 1/2 * Q:风量 * 风的密度(常数) * v风实际^2 / (60gn)
# g 重力加速度(常数) n 封口数(常数)

# v实 = v标 * (t+273) * 0.1013 /( 0.1013+P风) /273
# t为风温 P风:热风压力

# E:鼓风动能 正比于 Q * [V标*(t+273)/(0.1013+P风)] ^2  
# 0.1013 Mpa
'''

def standardscale(data):
    '''
    标准差标准化 or
    min-max 标准化
    link: https://blog.csdn.net/Monk_donot_know/article/details/86479176
    '''
#    data=(data-data.min())/(data.max()-data.min())
    data=(data-data.mean())/data.std()
    return data 

# 数据读取
dataE = pd.read_excel(r'./report/西昌2#new送风系统.xlsx')
dataSi = pd.read_excel(r'./report/new铁水成分表.xlsx')

# 计算鼓风动能
temp = dataE['标准风速'] * (dataE['热风温度'] + 273) / (101.3+dataE['热风压力'])
temp = temp ** 2
E = dataE['送风风量'] * temp

Si = dataSi[dataSi.铁次号 < 2 * 1e7]['[Si]'] # 提取铁次号< 2e7



# 数据异常 缺失 处理
E[E>2e11] = np.nan  # 画图发现极端值
E = E.fillna(E.mean()) # 缺失值用均值填充

E = E[150:]  # 数据大块缺失!
Si = Si[150:]


# 标准化
E = standardscale(E)
Si = standardscale(Si)

length = len(E)
plt.plot(range(length), E)
plt.plot(range(length), Si)

# 给与 i倍的单位滞后 画图找出最大相关值时的 i
#   # 可惜Si采样的时间频率是 2 hour ---- 插值吗?
length = 12 # 最大可能的滞后
ans = np.zeros(length)
for i in range(length):
    ans[i] = Si[i:].corr(E[:-1-i])
ans = abs(ans)
plt.figure()
plt.plot(np.arange(0,length*2,2),ans)

print('为了数据对齐, 需要移动的表格单位数是: ', ans.argmax())
print(ans.max())
     
                       