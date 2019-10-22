import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,100)

y1 = x ** 2
y2 = 2 * x + 1

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1)

plt.xlim((-1,2))  # 范围
plt.ylim((-2,3))
plt.xlabel('I am x') # 标签
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           [r'$really\ bad$',r'$bad\ \alpha$',
            r'$normal$',r'$good$',r'$really\ good$'])

# gca = 'get current axis'
ax = plt.gca() #获得图框沿
ax.spines['right'].set_color('none') #spines 脊梁  让颜色消失
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')#设置上 x y轴
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',-1)) # 移动x轴 y轴
        #outward ,axes 类似于'data'的也是函数参数
ax.spines['left'].set_position(('data',0))

plt.show()









