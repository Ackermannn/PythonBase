# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:19:04 2019

@author: Administrator
"""
# numpy 常用功能
import numpy as np
a = np.array([1, 2, 5]) # 产生一个数组
out = a.shape
print("a的shape(形状为): ", out) #输出: a的shape(形状为):  (3,)

A = np.array([[0.5, 0.2, 0.3],
              [0.3, 0.5, 0.2],
              [0.2, 0.3, 0.5]])
out = A.shape
print("A的shape(形状为): ", out) #输出: A的shape(形状为):  (3, 3)  
# A.shape其实是个元组tuple 可以用访问listd的方式访问元组tuple
print(A.shape[0]) #输出: 3 ##访问元组的第0个
# 为啥a 是(3,) A 是(3,3)? 
# 当array() 小括号里只有一层[] a就是一维的 两层[[]] 就是两维的
# 可以输入一下命令查看 维度
out1 = a.ndim
out2 = A.ndim
print("a的维度是: {}, A的维度是: {}".format(out1, out2)) # a的维度是: 1, A的维度是: 2

# 练习
# 试试一下命令 
b = np.array([[1, 2]])
b.shape
b.ndim

# 输入一个矩阵要输入那么多方括号类似我了,有什么快捷的方法?
new_A = np.array([0.5, 0.2, 0.3, 0.3, 0.5, 0.2, 0.2, 0.3, 0.5]).reshape(3, 3)
# 试试 new_A 和 A 一样吗?
new_A2 = np.array([0.5, 0.2, 0.3, 0.3, 0.5, 0.2, 0.2, 0.3, 0.5]).reshape(1, 9)
# 看看new_A2 变成了什么
# 对 reshape(n, m) 就是把 array 变成 n * m 维

# 那矩阵乘法如何实现呢
A = np.arange(9).reshape(3,3)
'''
A = 
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
'''
B = np.arange(1,10).reshape(3,3)
'''
B = 
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
'''
# np.arange(9) 与 range(9) 类似 生成 0-8 的数组
# np.arange(1,9) 与 range(1,9) 类似 生成 1-8 的数组

out = np.dot(A, B) # np.dot() 实现矩阵相乘
print(out)
'''
输出:
[[ 18  21  24]
 [ 54  66  78]
 [ 90 111 132]]
'''
out = A * B # 这样是对应乘
print(out)
'''
输出:
[[ 0  2  6]
 [12 20 30]
 [42 56 72]]
'''
## 矩阵转置
A = np.arange(9).reshape(3, 3)
'''
Out[122]: 
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
'''
A.T 
A.transpose() # 两个是一样的
'''
Out[123]: 
array([[0, 3, 6],
       [1, 4, 7],
       [2, 5, 8]])
'''

# max, argmax
a = np.array([1, 2, 3, 0])
a.max() # 与 max(a) 相同
a.min()
a.argmax() # 返回最大值的下标 a 中 a[2] = 3是最大的 所以返回 2
a.argmin()
# 类似 sum()求和 numpy 有 a.sum() 使用后者会更快一些
# a.sort() 等价 sort(a) 排序
a.mean() # 求平均值
A.trace() # 迹

##  差不多你想要的简单功能 在网上找 应该会找到 
##



## 介绍一下 切片  切片的操作 np.array 和 list 基本是一样的 参考网站 https://www.jianshu.com/p/15715d6f4dad
a = np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[0] # a的第0个 # Out[119]: 0
a[-4] # a的倒数第四个 #  Out[119]: 6
a[:] #从左往右 # Out[124]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[::-1] #从右往左 # array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) 也就是倒序
a[1:6] # Out[126]: array([1, 2, 3, 4, 5]) 从1到 6-1
a[:6] # array([0, 1, 2, 3, 4, 5]) 从头单6-1
a[6:] # array([6, 7, 8, 9]) 从6到尾
# a[这里是开始索引:这里是结束索引:这是step/(几个几个数?)]

a[1:-1:2] # 猜猜输出多少????

# 可以连续切片
a[:8][2:5][-1:]
#相当于：
#a[:8]=[0, 1, 2, 3, 4, 5, 6, 7]
#a[:8][2:5]= [2, 3, 4]
#a[:8][2:5][-1:] = 4


# 很重要!!!!
a = np.arange(10)
print(a) # [0 1 2 3 4 5 6 7 8 9]
b = a
print(b) # [0 1 2 3 4 5 6 7 8 9]
b[0] = 99
print(a) # [99  1  2  3  4  5  6  7  8  9]
# 为啥b 也跟着变了
#可以试试这个命令
a is b 
# Out[132]: True
id(a)
#Out[133]: 1692231906688
id(b)
#Out[134]: 1692231906688
## 其实为了节省内存 b = a 其实是给 a 起了个小名 叫 b 如同给 你起了个小名,叫那个都是你,修改哪个,都会变

# 如果是 b = a.copy() 
a = np.arange(10)
print(a) # [0 1 2 3 4 5 6 7 8 9]
b = a.copy()
print(b) # [0 1 2 3 4 5 6 7 8 9]
b[0] = 99
print(b) # [99  1  2  3  4  5  6  7  8  9] 
print(a) # [0 1 2 3 4 5 6 7 8 9] 这样也正常了