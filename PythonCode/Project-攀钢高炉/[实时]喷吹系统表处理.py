# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:50:14 2019

@author: Ackerman
"""

import pandas as pd
import numpy as np


# read excel 
sys_blow = pd.read_excel('.\origin\西昌2#高炉采集数据表_喷吹系统.xlsx')
                         
                         
                         
                         
                         
                        
sys_blow = sys_blow.sort_values(by = '业务处理时间') ## 排序
temp = sys_blow['业务处理时间']  
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

new_sys_blow =  pd.merge(gr, sys_blow, left_index=True,right_index=True) # 和老表合并一下

# pivot
new_sys_blow = new_sys_blow.pivot_table(index='采集时段', 
              columns='采集项名称', values='采集项值',
              aggfunc = [np.mean,np.max]) # 日喷煤量是个累计数值
new_sys_blow.drop(
        columns = [('mean','日喷煤量'),
                   ('amax','喷吹速率')]
        ).to_excel(
                   r'./report/西昌2#new喷吹系统.xlsx')  














                    