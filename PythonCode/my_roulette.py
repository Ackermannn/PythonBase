# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:53:09 2019

@author: Administrator
"""
## my常用函数库 
## 轮盘赌函数
import numpy as np
from numpy import cumsum
from numpy.random import rand
def roulette(p):
    cum = cumsum(p)
    pr = rand()
    for i,item in enumerate(cum):
        if pr < item:
            return i
        
if __name__ == '__main__':
    p = np.array([0.3, 0.3, 0.4])
    print(roulette(p)) # 输出 在 0 1 2范围