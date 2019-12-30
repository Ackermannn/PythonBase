# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:52:26 2019

@author: Ackerman
"""

# 处理多 sheet 的情况
import pandas as pd

def load_excel(path, sheets = 2):
    if sheets == 1:
        file = pd.read_excel(path)
    else:
        file = pd.read_excel(path, sheet_name = None, header = None)
        file = pd.concat(file)
        file.columns = list(file.iloc[0])
        file = file.drop(index=file.index[0])      
    return file
        
f = load_excel('样本.xlsx')


