# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:06:52 2019

@author: Administrator
"""
import numpy as np
A = [[1,1,1,0],
     [2,1,0,1]];
A = np.array(A)
njnums = 2
b = np.array([40,60]).reshape(2,1)
c = np.array([-3,-2,0,0]).reshape(4,1)
x= np.array([0,0,40,60]).reshape(4,1) 
B= np.eye(2)
#IB=
cB= [0, 0]
cB = np.array(cB).reshape(2,1)


#for ii in range(100):
# step 1

w = np.linalg.inv(B.T).dot(cB)

# step 2
r = np.zeros((2,1))
for i in range(njnums):
    r[i] = c[i] - np.dot(w.T,A[:,i])
    #    r2 = c[1] - np.dot(w.T,A[:,1])
        
    # at least one r is samll than zero, it is not smalist !!!!  , we need 改进!!
        
    # step 5

    d = -1 * A[:,0]  # 急诊都是单位矩阵
        
    lamda = np.min(b / A[:,0:1])
    min_idx = np.argmin(b / A[:,0:1]) + njnums 
    # step 8
    x[0] = lamda
    x[1] = x[1]  
    x[2] = x[2] + lamda * d[0]
    x[3] = x[3] + lamda * d[1]



