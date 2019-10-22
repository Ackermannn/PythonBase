import numpy as np

b = [4,2,3,6]

a = [-1,-14,-6]

A0 = [[1,1,1],
      [1,0,0],
      [0,0,1],
      [0,3,1]]

b,a,A0 = np.array(b)[:,np.newaxis],np.array(a)[np.newaxis,:],np.array(A0) # list变矩阵
row0 = np.hstack(([[0]],a,np.zeros((1,b.shape[0]))))
row1 = np.hstack((b,A0,np.eye(b.shape[0])))
A = np.vstack((row0,row1))

print(A)
