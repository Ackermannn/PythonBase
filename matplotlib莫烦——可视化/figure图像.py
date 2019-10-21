import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,100)

y1 = x ** 2
y2 = 2 * x + 1

plt.figure('图1')
plt.plot(x, y1)

plt.figure('图2',figsize=(8,5)) # figsize 图形框大小
plt.plot(x, y2)
plt.plot(x, y1,color='red',linewidth=1.0,linestyle='--')
# color颜色
# linewidth 线宽
# linestyle 线型
plt.show()
