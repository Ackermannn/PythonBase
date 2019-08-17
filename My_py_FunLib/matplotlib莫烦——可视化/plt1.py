import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']='SimHei'
plt.figure(figsize=(8,5), dpi=80)
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C = np.cos(X)
S = np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
  [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
'''确定坐标范围
plt.axis([xmin, xmax, ymin, ymax])
axis()命令给定了坐标范围。
xlim(xmin, xmax)和ylim(ymin, ymax)来调整x,y坐标范围
'''
plt.ylim(C.min() * 1.1, C.max() * 1.1)
plt.yticks([-1, 0, +1],
  [r'bottom', r'normal', r'top'])
plt.annotate('local max',xy=(0,1),xytext=(1.2,1.2),
             arrowprops=dict(facecolor='red',shrink=0.04))
plt.xlabel('X轴',fontsize=12,color='red',rotation=60,verticalalignment='top')
plt.ylabel('y轴',fontsize=14,color='blue',rotation=30,horizontalalignment='center')
plt.text(-2,0.5,r'数学sin函数',rotation=30)
plt.savefig('spine.png')
plt.show()
#--------------------- 
#版权声明：本文为CSDN博主「NoOne-csdn」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_40161254/article/details/82866689
