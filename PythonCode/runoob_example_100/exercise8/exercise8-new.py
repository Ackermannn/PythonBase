# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:36:30 2019

@author: Administrator
"""

# -*- coding: UTF-8 -*-
for i in range(1,10):
    for j in range(1,i+1):
            print(' {}*{}={:2}'.format(i, j, i*j),end=',')
    print()