# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:04:21 2019

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

df = pd.read_pickle('time_process.pkl')
df = str2time(df)