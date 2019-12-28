# -*- coding: utf-8 -*-
"""
把炉渣表, 三个铁水验表合并起来

同一铁次分多个罐号 取值平均

还未处理异常值, 缺失值
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

zha = pd.read_excel('.\origin\炉渣成分表.xlsx')
iron_comp = pd.read_excel('.\origin\铁水成分表.xlsx')
iron_real = pd.read_excel('.\origin\铁水实绩表.xlsx')
iron_mass = pd.read_excel('.\origin\铁水质量表.xlsx')

## 数据旋转 
iron_comp = iron_comp.drop(columns=['系统接收时间','采集项编码','上料批号','班别','班次'])
new_iron_comp = iron_comp.pivot_table(index='铁次号', 
              columns='采集项名称', values='采集项值',
              aggfunc = np.mean)
new_iron_comp.to_excel(r'./report/new铁水成分表.xlsx')
#pd.merge(left, right, on='key')


## 数据旋转  受铁质量 只有2开头的铁次号
#iron_comp = iron_comp.drop(columns=['系统接收时间','采集项编码','上料批号','班别','班次'])
new_iron_real = iron_real.pivot_table(index='铁次号', 
              columns='采集项名称', values='采集项值',
              aggfunc = np.mean)   # 存在0的受铁质量??????
new_iron_real.to_excel(r'./report/new铁水实绩表.xlsx')

## 数据旋转 
new_iron_mass = iron_mass.pivot_table(index='铁次号', 
              columns='采集项名称', values='采集项值',
              aggfunc = np.mean)
new_iron_mass.to_excel('new铁水质量表.xlsx') # 许多数据缺失

new_zha = zha.pivot_table(index='铁次号', 
              columns='采集项名称', values='采集项值',
              aggfunc = np.mean)
new_zha.to_excel(r'./report/new炉渣成分表.xlsx')


# 大合并---也不太需要吧
out1 = pd.merge(new_iron_comp, new_iron_real, 
               left_index=True,right_index=True,how='outer')
out2 = pd.merge(new_iron_mass, new_zha, 
               left_index=True,right_index=True,how='outer')
out = pd.merge(out1, out2, 
               left_index=True,right_index=True,how='outer')

out.to_excel(r'./report/炉渣-铁水表.xlsx')