# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:33:02 2019

@author: Ackerman
"""
import pandas as pd
df = pd.read_pickle('chach.pkl')

# copy

#count = 10
df['业务处理时间'] = pd.to_datetime(df['业务处理时间'])

start = pd.to_datetime('2019-10-01 02:00:00')  
end = pd.to_datetime('2019-12-1 00:00:00')
tag = pd.date_range(start=start, end=end, freq='2H')


p = 0
gr = df['业务处理时间']
for  i in range(len(df)):
    if gr[i] <= tag[p]: 
        gr[i] = tag[p]
    else: 
        p = p + 1
        gr[i] = tag[p]