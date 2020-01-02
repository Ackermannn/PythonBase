# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:13:17 2020

@author: Ackerman
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
'''
跑矿累计到 2 小时内  
'''

mine_real = pd.read_excel('.\origin\上料实绩表.xlsx')


mine_real = mine_real.sort_values(by = '业务处理时间') ## 排序
temp = mine_real['业务处理时间']  
#temp = pd.DataFrame(temp)
gr = pd.to_datetime(temp)

start = pd.to_datetime('2019-10-01 02:00:00')  
end = pd.to_datetime('2019-12-1 00:00:00')
tag = pd.date_range(start=start, end=end, freq='2H')

p = 0
for  i in range(len(gr)):
    if gr[i] <= tag[p]: 
        gr[i] = tag[p]
    else: 
        p = p + 1
        gr[i] = tag[p]


gr = pd.DataFrame(gr)
gr = gr.rename(columns ={'业务处理时间':'采集时段'})  # 改个名字

new_mine_real =  pd.merge(gr, mine_real, left_index=True,right_index=True) # 和老表合并一下

# pivot
new_mine_real = new_mine_real.pivot_table(index='采集时段', 
              columns='采集项名称', values='采集项值',
              aggfunc = np.sum)   # 注意这里用的是 sum
new_mine_real.to_excel(r'./report/new上料实绩表.xlsx')

