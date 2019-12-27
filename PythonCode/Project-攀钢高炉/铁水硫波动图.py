'''
把铁水成分表中的 [s] 采集项目 抽离出来 画出 铁次号 开头 1 2 3 的波动图


罐子号?
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

iron_comp = pd.read_excel('.\origin\铁水成分表.xlsx')

iron_S = iron_comp[iron_comp.采集项名称 == '[S]'] # 筛选出 [S]

iron_S = iron_S.sort_values(by='铁次号') # 对铁次号排序

## 对铁次号分组
iron1 = iron_S[round(iron_S.铁次号/1e7) == 1]
iron2 = iron_S[round(iron_S.铁次号/1e7) == 2]
iron3 = iron_S[round(iron_S.铁次号/1e7) == 3]


#开启一个窗口，num设置子图数量，figsize设置窗口大小，dpi设置分辨率
fig = plt.figure(num=3, figsize=(15, 8),dpi=80) 
#直接用plt.plot画图，第一个参数是表示横轴的序列，第二个参数是表示纵轴的序列 
ax1 = fig.add_subplot(3,1,1)  
ax2 = fig.add_subplot(3,1,2)  
ax3 = fig.add_subplot(3,1,3)  
x = range(len(iron1['采集项值']))
ax1.plot(x, iron1['采集项值'])
x = range(len(iron2['采集项值']))
ax2.plot(x, iron2['采集项值'])
x = range(len(iron3['采集项值']))
ax3.plot(x, iron3['采集项值'])
#显示绘图结果
plt.show()
