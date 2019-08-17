import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 0.1 * x

plt.figure()
plt.plot(x,y,linewidth = 10,zorder=1) # zorder z order 图层叠放顺序
plt.ylim(-2,2)

ax = plt.gca() # gca = get current axes  axes:轴
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置底边的移动范围，移动到y轴的0位置
# data:移动轴的位置到交叉轴的指定坐标  outward:不太懂  axes:0.0 - 1.0之间的值，整个轴上的比例  center:('axes',0.5) zero:('data',0.0)

ax.xaxis.set_ticks_position('bottom') 
ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)  #变大
    label.set_bbox(dict(facecolor='white',
                        edgecolor='none',
                            alpha=0.7,zorder=2)) #alpha透明的
plt.show()









