import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
print('====矩阵加减====')
print('a=\n',a)
print('b=\n',b)
c = a - b
print('a - b = \n',c)

# a + b
#####################################
c = b**2 #b的平方
print('b**2 =\n',c)

c = 10*np.sin(a)
print('10*np.sin(a)=\n',c)

print('b<3 \n',b<3)
#####################################
print('====矩阵乘法====')
a = np.array([[10,20],
             [30,40]])
b = np.arange(4).reshape((2,2))
print('a=\n',a)
print('b=\n',b)
c = a*b #逐个相乘
print('a*b=\n',c)
c_dot = np.dot(a,b)# 矩阵运算
print('np.dot(a,b)=\n',c_dot)
c_dot2 = a.dot(b)# 矩阵运算2
print('a.dot(b)=\n',c_dot2)
###########

a = np.random.random((2,4)) # 随机产生范围[0,1]
np.sum(a) #求和
np.sum(a,axis=1) #求和 axis=1 在列求和  axis = 0 在行操作
np.min(a) #求最小
np.max(a) #求最大















