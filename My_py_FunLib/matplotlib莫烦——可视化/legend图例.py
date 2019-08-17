import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,100)
y1 = x ** 2
y2 = 2 * x + 1

plt.figure()
l1 = plt.plot(x, y1,label='up')
l2 = plt.plot(x, y2,label='down')
plt.legend()

plt.show()









