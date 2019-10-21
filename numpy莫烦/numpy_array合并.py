import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])
print('A =\n',A)
print('B =\n',B)
C2 = np.vstack((A,B)) #上下合并 可以三个合并
D2 = np.hstack((A,B)) #左右合并
print('C2 = np.vstack((A,B)) = #上下合并:\n',C2)
print('D2 = np.hstack((A,B)) = #左右合并:\n',D2)
print('A.shape =,C2.shape =,D2.shape =')
print(A.shape,C2.shape,D2.shape)


print(A[:,np.newaxis].shape) # 此时A不是0*3维，而成为1*3维
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
C = np.concatenate((A,B,B,A),axis=1)
print(C)

#### my way shape为(3,) 变(1,3) 
A = np.array([1,1,1])
print(A.shape)
A2 = A.reshape(1,A.shape[0])
print(A2.shape)
'''
np.vstack()
np.hstack()
np.concatenate()
'''
