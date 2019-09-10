# My simple merul network
import numpy as np
import matplotlib.pyplot as plt


def relu(x): # 输入的是矩阵
    return 1/(1+np.exp(-x))

def hidden_layer(input_date,theta1):
    input_date = np.hstack((np.ones((1,1)) ,input_date))
    return relu(np.dot(input_date,theta1))   # hidden layer have five nerves 100*3 3*5 -> 100* 5

def out_layer(input_date,theta2):
    input_date = np.hstack((np.ones((1,1)) ,input_date))
    return relu(np.dot(input_date,theta2)) # 100*6  6*1 -> 100*1

def nerve_fun(input_date,theta1,theta2):
    hidde_out = hidden_layer(input_date,theta1)
    out = out_layer(hidde_out,theta2)
  #  out = np.floor(out+0.5)
    return out

def cost(theta1, theta2, data_x, data_y):
    return np.sum((data_y - nerve_fun(data_x,theta1,theta2))**2)    # 误差计算


# creat data
x = np.random.uniform(low=-1,high=1,size=(100,1))
##y = np.random.uniform(low=-1,high=1,size=(100,1))
##data_x = np.hstack((x,y))
data_x = x
noise = np.random.uniform(low=-0.2,high=0.2,size=(data_x.shape[0],1))
data_y = x**2 + noise
##for i in range(100):
##    if np.sqrt(x[i]**2 + y[i]**2) <= 1:
##        data_y[i] = 1
##    else:
##        data_y[i] = 0


# 参数初始化

theta1 = np.random.uniform(low=0,high=1,size=(2,10)) # 3行5列 第一行是偏置
theta2 = np.random.uniform(low=0,high=1,size=(11,1))
learning_rate = 100

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(data_x, data_y)  # 蓝色散点是数据点 
lines = ax.plot(data_x, nerve_fun(data_x,theta1,theta2) ,c = 'r')
plt.ion()
plt.show()

# train
for index in range(1000):
    for s in range(100): # 对样本循环 
        hidde_out = hidden_layer(data_x[s],theta1)
        out = nerve_fun(data_x[s,0],theta1,theta2)
        g = (data_y - out) * out * (1-out)
        
        for i in range(10):  # train theta1
            theta1[0,i] -= learning_rate * np.mean( hidde_out[:,0] *(1-hidde_out[:,0]) *theta1[0,i] *g  )    
            for j in range(1,2):
                theta1[j,i] += learning_rate * np.mean(
                    hidde_out[:,j] *(1-hidde_out[:,j]) *theta1[j,i] *g *data_x[:,j-1]
                    )    # 目前只有一个输出
            
        
        theta2[0,0] -= learning_rate * np.mean(g)     
        for i in range(1,11): # train theta2
            theta2[i,0] += learning_rate * np.mean(g * hidde_out[:,i-1])


    #print(nerve_fun(data_x,theta1,theta2))
    if index % 50 == 1:
        print(cost(theta1, theta2, data_x, data_y))
        ax.lines.remove(lines[0])
        lines = ax.plot(data_x, out, c = 'r')
        plt.pause(0.1)


# text
##x = np.random.uniform(low=-1,high=1,size=(100,1))
##y = np.random.uniform(low=-1,high=1,size=(100,1))
##Tdata_x = np.hstack((x,y))
##
##Tdata_y = np.zeros((100,1))
##for ii in range(100):
##    if np.sqrt(x[ii]**2 + y[ii]**2) <= 0.75:
##        Tdata_y[ii] = 1
##    else:
##        Tdata_y[ii] = 0
##
##    out = nerve_fun(Tdata_x,theta1,theta2)
##    out = np.floor(out+0.5)
##temp = list( out == Tdata_y)
##print(temp.count(True))
print(theta1)
print(theta2)
##
