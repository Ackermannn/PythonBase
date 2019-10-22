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

# r'$bad\ \alpha$'   \alpha 打印数学形式的alpha




plt.show()









