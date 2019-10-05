# 实现单纯型法的矩阵运算
# 教程网址
# https://www.hrwhisper.me/introduction-to-simplex-algorithm/
# 要求b都大于零！！！，即初始解是基本可行解
import numpy as np
def solve(A):
    while 1:
        for i in range(1,A.shape[1]): # 找到要增大的x,即找第一行中是负值的数的index
            if A[0,i] < 0:
                New_x_index = i;
                break;
            
        constrain = np.inf;operation_row = 1;
        for i in range(1,A.shape[0]):   #进而 寻找 约束性强的行  
            if A[i,New_x_index] > 0 and A[i,0]/A[i,New_x_index] < constrain:
                constrain = A[i,0]/A[i,New_x_index];
                operation_row = i;

        A[operation_row,:] /= A[operation_row,New_x_index];
        for i in range(A.shape[0]):    #  行变换
            if i != operation_row: 
                A[i,:] += -1 * A[i,New_x_index] * A[operation_row,:]
        
        if (A[0,:] >= 0).all(): # 如果没有x 能增大 结束
            break;
    return A

def find_x(A):
    j = 1;x = A[0,1:]
    for i in range(1,A.shape[1]):
        if A[0,i] != 0:
            x[i-1] = 0
        else:
            x[i-1] = A[j,0]
            j += 1
    return x;

'''
list1 =['对于以下线性规划问题的求解:',
'min z = -x1 - 14*x2 -6*x3',
's.t.',
'x1 + x2 + x3 <= 4',
'          x1 <= 2',
'          x3 <= 3',
'   3*x2 + x3 <= 6',
'    x1,x2,x3 >=0',
]
for i in list1:
    print(i)
'''

# b = [4,2,3,6]

#a = [-1,-14,-6]

#A0 = [[1,1,1],
#      [1,0,0],
#      [0,0,1],
 #     [0,3,1]]

#b,a,A0 = np.array(b)[:,np.newaxis],np.array(a)[np.newaxis,:],np.array(A0) # list变矩阵
#row0 = np.hstack(([[0]],a,np.zeros((1,b.shape[0]))))
#row1 = np.hstack((b,A0,np.eye(b.shape[0])))
#A = np.vstack((row0,row1))

#print(A)
#A = [[0,-1,-14,-6,0,0,0,0],
#     [4, 1,  1, 1,1,0,0,0],
#     [2, 1,  0, 0,0,1,0,0],
#     [3, 0,  0, 1,0,0,1,0],
#     [6, 0,  3, 1,0,0,0,1]]

A = [[0,-3,-2,0,0],
     [40,1, 1,1,0],
     [60,2, 1,0,1]]
A = np.array(A,dtype = float)

solve_A = solve(A)
#print(solve_A)
x = find_x(solve_A)
##
print('最小值是:',-1*solve_A[0,0])
print('此时的解向量:',x)
##        
##    
