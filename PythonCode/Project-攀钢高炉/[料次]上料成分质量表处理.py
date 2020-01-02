# -*- coding: utf-8 -*-
"""
对于上料成分表 mine_comp
把 化验采集时间作为 index 

    从上料批号里发掘上料时间
    以此为例子:
    191001S000001-2201
    
    191001 指19年10月1日
                 -2201 指22点进行采样
                 
把 各个采集项 作为 column

若有冲突(同一 index column 有两个不同数值, 取平均---  本人猜测攀钢就是同一批次的多次测量)
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def str2time(df):
    '''
    df: pandas.Series类
    
    从上料批号里发掘上料时间
    '''
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


def mine_order(path_r, path_s):
    '''
    path_r: 读取的路径
    path_s: 保存的路径
    对带有铁次号的表的数据规整.即, index 为铁次号 与 日期, column'采集项名称','采集项编码'
    
    '''
    df = pd.read_excel(path_r)
    
    se = df['上料批号'].copy() # 拷贝一份 防止崩溃
    se = str2time(se) # 调用子函数 对str 处理成时间格式
    se = pd.DataFrame(se) 
    se = se.rename(columns ={'上料批号':'采料时间'})  # 改个名字
    df =  pd.merge(se, df, left_index=True,right_index=True) # 和老表合并一下
    
    df = df.pivot_table(index=['采料时间','业务处理时间'], # 猜测铁次号第一位数字代表样本号
              columns=['采集项名称','采集项编码'], values='采集项值',
              aggfunc = np.mean)
    df.to_excel(path_s)


if __name__ == '__main__':
    
    path_r = [r'./origin/上料成分表.xlsx',
              r'./origin/上料质量表.xlsx']
    
    path_s = [r'./report/new上料成分表.xlsx',
              r'./report/new上料质量表.xlsx']
    for i in range(len(path_r)):
         mine_order(path_r[i], path_s[i])


    """
    虽然表中会出现很多 nan 但是在提取变量时可以利用一下代码去掉nan
    path_r = r'./report/new上料质量表.xlsx'
    df = pd.read_excel(path_r, index_col=[0,1], header = [0,1])
    temp = df['45褐铁块矿_25-40mm粒度']
    temp = temp.dropna()
    """