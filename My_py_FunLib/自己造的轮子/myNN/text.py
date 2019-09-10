# My simple merul network
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale


def relu(x):  # 输入的x 为列向量
    b = np.zeros((x.shape[0],1))
    c = np.hstack((x,b))
    return np.max(c,axis =1)
    
def sigma(x): 
    return 1/(1+np.exp(-x))

def hidden_layer(input_data):
    return relu(np.dot(input_data,w1)-b1) # input_data是单个样本

def out_layer(input_date):
    return np.sum(input_date*w2.T)-b2 # 100*6  6*1 -> 100*1

def nerve_fun(input_date):
    hidde_out = hidden_layer(input_date)
    out = out_layer(hidde_out)
    return out

def cost(data_x, data_y):
    y_pre = np.zeros((100,1))
    for i in range(100):
        y_pre[i,0] = nerve_fun(data_x[i,0])
    return np.mean((data_y - y_pre)**2)    # 误差计算


# creat data
x = np.random.uniform(low=0,high=1,size=(100,1))
data_x = x
noise = np.random.uniform(low=-0.05,high=0.05,size=(data_x.shape[0],1))
data_y = x**3 + noise


# 参数初始化

w1 = np.random.uniform(low=-1,high=1,size=(10,1))  # 
b1 = np.random.uniform(low=-1,high=1,size=(10,1))  # 10个隐藏神经元
w2 = np.random.uniform(low=-1,high=1,size=(10,1))  # 
b2 = np.random.uniform(low=-1,high=1,size=(1,1))   # 1个输出神经元
learning_rate = 0.01

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
  
y_pre = np.zeros((100,1))
x = np.linspace(0,1,100).reshape(100,1)

for i in range(100):
    y_pre[i,0] = nerve_fun(x[i,0])
    
ax.plot(x, y_pre)     
plt.show()

