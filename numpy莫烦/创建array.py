import numpy as np

a = np.array([2,23,4])
print(a) # 没有逗号分隔

a = np.array([2,23,4],dtype=np.int) #dtype=np.float64
print(a.dtype)

'''
dtype类型
int8,16,32,64
float16,32,64,128
complex64,128,256
bool
object
'''

a = np.array([[2,23,4],
              [1, 3,0]])
print(a)

a = np.zeros((3,4)) #注意要用括号
print(a) #三行四列的0

a = np.ones((3,4),dtype=np.int)
print(a)

a = np.empty((3,4)) #其实是几乎为0的数
print(a)

a = np.arange(10,20,2) 
print(a)#[10 12 14 16 18]

a = np.arange(12).reshape((3,4))
print(a)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

a = np.linspace(1,10,5)
print('\nnp.linspace(1,10,5)=')
print(a)



