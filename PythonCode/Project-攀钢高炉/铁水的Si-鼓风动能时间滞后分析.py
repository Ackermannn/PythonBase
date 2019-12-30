# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:43:36 2019

@author: Ackerman
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
'''
# 系数并不影响 相关系数! 

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
    标准差标准化
    link: https://blog.csdn.net/Monk_donot_know/article/details/86479176
    '''
#    data=(data-data.min())/(data.max()-data.min())
    data=(data-data.mean())/data.std()
    return data 

dataE = pd.read_excel(r'./report/西昌2#new送风系统.xlsx')

dataSi = pd.read_excel(r'./report/new铁水成分表.xlsx')


                      
temp = dataE['标准风速'] * (dataE['热风温度'] + 273) / (101.3+dataE['热风压力'])
temp = temp ** 2
E = dataE['送风风量'] * temp

Si = dataSi[dataSi.铁次号 < 2 * 1e7]['[Si]']



# 数据异常 缺失 处理
E[E>2e11] = np.nan
E = E.fillna(E.mean())
E = E[150:]
Si = Si[150:]
# 标准化
E = standardscale(E)
Si = standardscale(Si)

length = len(E)
plt.plot(range(length), E)

plt.plot(range(length), Si)


length = 12 # 最大可能的滞后
ans = np.zeros(length)
for i in range(length):
    ans[i] = Si[i:].corr(E[:-1-i])
#    print(ans[i])
plt.figure()

plt.plot(np.arange(0,length*2,2),abs(ans))

print(ans.argmax())
print(ans.max())
     
                       