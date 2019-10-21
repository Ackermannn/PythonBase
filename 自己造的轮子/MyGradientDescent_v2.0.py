# my simple merul network
import numpy as np
import matplotlib.pyplot as plt


def h(x, theta):
    return theta[2] * x * x +  theta[1] * x  + theta[0]   # 要拟合的函数

def cost(theta, data_x, data_y):
    return 1.0/2/data_x.shape[0] * np.sum((data_y - h(data_x, theta))**2)    # 误差计算

# 数据导入
data_x = np.arange(-10,10,0.2)[:,np.newaxis]              
noise = np.random.uniform(low=-2,high=2,size=(data_x.shape[0],1))
data_y = 1 * data_x**2 - 2 * data_x + 1 + noise

# 参数初始化
theta = 0.1 * np.ones((3,1))

# 画图
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(data_x, data_y)  # 蓝色散点是数据点 
lines = ax.plot(data_x, h(data_x, theta) ,c = 'r')
plt.ion()
plt.show()
学习率 = 0.001

for i in range(1000):
    theta[2] -= 学习率 * 1.0/2/data_x.shape[0] * np.sum((h(data_x, theta) - data_y) * data_x**2)
    theta[1] -= 学习率 * 1.0/2/data_x.shape[0] * np.sum((h(data_x, theta) - data_y) * data_x) # 梯度下降法参数a的更新
    theta[0] -= 学习率 * 1.0/2/data_x.shape[0] * np.sum((h(data_x, theta) - data_y) * 1)      # 梯度下降法参数b的更新
    if i % 50 == 0:
        print('cost=', cost(theta, data_x, data_y))
        ax.lines.remove(lines[0])
        lines = ax.plot(data_x, h(data_x, theta), c = 'r')
        plt.pause(0.1)
print('theta=',theta,sep='\n')

