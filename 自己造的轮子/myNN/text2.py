# 向量合并


import numpy as np
##a = np.array([0,9,88])[:,np.newaxis]
##b = np.array([1,8,3])[:,np.newaxis]
##c = np.hstack((a,b))
##
##print(np.max(c,axis =1))
def relu(x):
    b = np.zeros((x.shape[0],1))
    c = np.hstack((x,b))
    return np.max(c,axis =1)

x = np.array([1 , 2 ,-9, 0]).reshape(4,1)
out  = relu(x)
