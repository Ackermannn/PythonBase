import numpy as np

A = np.random.randint(10,size=(3,4))
print('A=\n',A)
print('np.argmin(A)=\n',np.argmin(A)) # 返回最索引
print('np.argmax(A)=\n',np.argmax(A)) # 返回最索引
print('np.average(A)=\n',np.average(A))
print('np.median(A)=\n',np.median(A))
print('np.cumsum(A)=\n',np.cumsum(A))
print('np.diff(A) =\n',np.diff(A) )
print('np.nonzero(A)=\n',np.nonzero(A))
print('np.sort(A)=\n',np.sort(A))
print('np.transpose(A)=\n',np.transpose(A))
print('np.clip(A,5,9)=\n',np.clip(A,5,9))
print('np.mean(A)=\n',np.mean(A))
print('np.mean(A,axis=0)=\n',np.mean(A,axis = 0))

'''
np.argmin(A) 最小值的索引
np.argmax(A)最大的索引
np.average(A) 所有元素平均值
np.median(A) 中位数
np.cumsum(A) 累计加，前缀和
np.diff(A)   累差
np.nonzero(A) 非零
np.sort(A)    排序
np.transpose(A) 转置 或者写 A.T
np.clip(A,5,9)
np.mean(A)
'''
