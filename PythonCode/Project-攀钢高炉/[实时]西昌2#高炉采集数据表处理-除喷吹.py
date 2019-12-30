# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:46:22 2019

@author: Ackerman
"""

import pandas as pd
import numpy as np


# 应付多 sheet 的情况
def load_excel(path, sheets = 2): 
    if sheets == 1:
        file = pd.read_excel(path)
    else:
        file = pd.read_excel(path, sheet_name = None, header = None)
        file = pd.concat(file)
        file.columns = list(file.iloc[0])
        file = file.drop(index=file.index[0])      
    return file

# 主程序
def summary_2H(s, out_s): 
    # read excel 
    sys = load_excel(s)
    sys = sys.sort_values(by = '业务处理时间') ## 排序
    
    temp = sys['业务处理时间'] 

    gr = pd.to_datetime(temp)
    start = pd.to_datetime('2019-10-01 02:00:00')  
    end = pd.to_datetime('2019-12-1 00:00:00')
    tag = pd.date_range(start=start, end=end, freq='2H') # 产生时段
    
    p = 0
    for  i in range(len(gr)):
        if gr[i] <= tag[p]: 
            gr[i] = tag[p]
        else: 
            p = p + 1
            gr[i] = tag[p]
    
    
    gr = pd.DataFrame(gr)
    gr = gr.rename(columns ={'业务处理时间':'采集时段'})  # 改个名字
    
    new_mine_real =  pd.merge(gr, sys, left_index=True,right_index=True) # 和老表合并一下
    
    # 数据表的pivot
    
    # 如果 采集数值不是数字 要进行转化
    if (new_mine_real['采集项值'].dtypes == 'O') :
        new_mine_real['采集项值'] = new_mine_real['采集项值'].apply(pd.to_numeric)
        
    new_mine_real = new_mine_real.pivot_table(index='采集时段', 
                  columns='采集项名称', values='采集项值',
                  aggfunc = np.mean)
    new_mine_real.to_excel(out_s)


# 给出读取 输出的路径
    
#s = '.\origin\西昌2#高炉采集数据表_高炉本体(炉顶,炉喉,炉身,炉腹).xlsx'
#out_s = r'./report/西昌2#new高炉本体0.xlsx'
#summary_2H(s, out_s)

s = '.\origin\西昌2#高炉采集数据表_高炉本体(炉缸1).xlsx'
out_s = r'./report/西昌2#new高炉本体1.xlsx'
summary_2H(s, out_s)

s = '.\origin\西昌2#高炉采集数据表_高炉本体(炉缸2).xlsx'
out_s = r'./report/西昌2#new高炉本体2.xlsx'
summary_2H(s, out_s)

s = '.\origin\西昌2#高炉采集数据表_高炉本体(炉缸3).xlsx'
out_s = r'./report/西昌2#new高炉本体3.xlsx'
summary_2H(s, out_s)

s = '.\origin\西昌2#高炉采集数据表_高炉本体(炉缸4).xlsx'
out_s = r'./report/西昌2#new高炉本体4.xlsx'
summary_2H(s, out_s)

                         
#s = '.\origin\西昌2#高炉采集数据表_上料系统.xlsx'
#out_s = r'./report/西昌2#new上料系统.xlsx'
#summary_2H(s, out_s)
##
#s = '.\origin\西昌2#高炉采集数据表_送风系统.xlsx'
#out_s = r'./report/西昌2#new送风系统.xlsx'
#summary_2H(s, out_s)
#
#s = '.\origin\西昌2#高炉采集数据表_渣铁系统.xlsx'
#out_s = r'./report/西昌2#new渣铁系统.xlsx'
#summary_2H(s, out_s)
