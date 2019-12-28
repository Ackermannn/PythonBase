# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:29:47 2019

@author: Ackerman
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def str2time(df):
    for i,item in enumerate(df):
        year = '20' + item[:2]
        month = item[2:4]
        
        day = item[4:6]
        hour = item[-4:-2]
        
        if hour == '24':
            hour = '23'
            # 10-01 24:00:00 的错误处理
            df[i] = pd.to_datetime( year+'-'+month+'-'+day+' '+hour+'5959') + +pd.Timedelta(seconds=1)
        else:    
            df[i] = pd.to_datetime( year+'-'+month+'-'+day+' '+hour)
    return df


mine_comp = pd.read_excel('.\origin\上料成分表.xlsx')
mine_real = pd.read_excel('.\origin\上料实绩表.xlsx')
mine_qual = pd.read_excel('.\origin\上料质量表.xlsx')

'''
对于上料成分表 mine_comp
把 化验采集时间作为 index 

    从上料批号里发掘上料时间
    以此为例子:
    191001S000001-2201
    
    191001 指19年10月1日
                 -2201 指22点进行采样
                 
把 各个采集项 作为 column

若有冲突(同一 index column 有两个不同数值, 取平均---  本人猜测攀钢就是同一批次的多次测量)

'''


################################ 上料成分表################################

# 首先对上料批次号处理一下
df = mine_comp['上料批号'].copy() # 拷贝一份 防止崩溃
df = str2time(df) # 调用子函数 对str 处理成时间格式
df = pd.DataFrame(df) 
df = df.rename(columns ={'上料批号':'采料时间'})  # 改个名字
new_mine_comp =  pd.merge(df, mine_comp, left_index=True,right_index=True) # 和老表合并一下
# pivot
new_mine_comp = new_mine_comp.pivot_table(index='采料时间', 
              columns='采集项名称', values='采集项值',
              aggfunc = np.mean)
new_mine_comp.to_excel('.\report\new上料成分表.xlsx')


################################# 上料质量表  ###########################
'''
同上
'''
# 首先对上料批次号处理一下
df = mine_qual['上料批号'].copy() # 拷贝一份 防止崩溃
df = str2time(df) # 调用子函数 对str 处理成时间格式
df = pd.DataFrame(df) 
df = df.rename(columns ={'上料批号':'采料时间'})  # 改个名字
new_mine_qual =  pd.merge(df, mine_qual, left_index=True,right_index=True) # 和老表合并一下
# pivot
new_mine_qual = new_mine_qual.pivot_table(index='采料时间', 
              columns='采集项名称', values='采集项值',
              aggfunc = np.mean)
new_mine_qual.to_excel('.\report\new上料质量表.xlsx')

############################### 上料实绩表  #############################
'''
跑矿累计到 2 小时内  
'''
#save = new_mine_real.index
#save = pd.DataFrame(save)
#save.to_pickle('chach.pkl')

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
              aggfunc = np.sum)
new_mine_real.to_excel('.\report\new上料实绩表.xlsx')


# 大合并
out = pd.merge(new_mine_comp, new_mine_qual, 
               left_index=True,right_index=True,how='outer')
out = pd.merge(out, new_mine_real,
               left_index=True,right_index=True,how='outer')
out.to_excel('.\report\矿料表.xlsx')
