# My simple merul network
import numpy as np
import matplotlib.pyplot as plt

def sigma(x): 
    return 1/(1+np.exp(-x))

def hidden_layer(input_data):
    return sigma(np.dot(input_data,w1)-b1) # input_data是单个样本

def out_layer(input_date):
    return sigma(np.sum(input_date*w2.T)-b2) # 100*6  6*1 -> 100*1

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
x = np.random.uniform(low=-1,high=1,size=(100,1))
data_x = x
noise = np.random.uniform(low=-0.2,high=0.2,size=(data_x.shape[0],1))
data_y = 0.5*x+0.15 + noise



# 参数初始化

w1 = np.random.uniform(low=0,high=1,size=(10,1))  # 
b1 = np.random.uniform(low=0,high=1,size=(10,1))  # 10个隐藏神经元
w2 = np.random.uniform(low=0,high=1,size=(10,1))  # 
b2 = np.random.uniform(low=0,high=1,size=(1,1))   # 1个输出神经元
learning_rate = 0.01

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(data_x, data_y)  # 蓝色散点是数据点

y_pre = np.zeros((100,1))
for i in range(100):
    y_pre[i,0] = nerve_fun(data_x[i,0])
    
lines = ax.plot(data_x, y_pre,c = 'r')
plt.ion()
plt.show()

# train
for index in range(2):
    for s in range(100): # 对样本循环
        
        hidde_out = hidden_layer(data_x[s,0])
        out = nerve_fun(data_x[s,0])
        g = (data_y[s,0] - out) * out * (1-out)
        
        # train b1
        for i in range(10):
            deta_b1  = learning_rate * hidde_out[i,0] * (1 - hidde_out[i,0]) * g * w1[i,0]
            b1[i,0] -= deta_b1
            
        # train w1
        for i in range(10):
            w1[i,0] += learning_rate * hidde_out[i,0] * (1 - hidde_out[i,0]) * g * w1[i,0] * data_x[s,0] 
            
        # train b2
        b2 -= learning_rate * g

        # train w2   
        for i in range(10):
            w2[i,0] += learning_rate * g * hidde_out[i,0]
    

        if s%25 == 0:
            print('cost = ',cost(data_x, data_y))
            ax.lines.remove(lines[0])
                
            y_pre = np.zeros((100,1))
            for i in range(100):
                y_pre[i,0] = nerve_fun(data_x[i,0])
                    
            lines = ax.plot(data_x, y_pre,c = 'r')
            plt.pause(0.1)

# print('w1,b1,w2,b2 = ',w1,b1,w2,b2,sep='\n')

print(nerve_fun(-1))
#
