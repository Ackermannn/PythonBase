import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_excel('样本2.xlsx')

df.corr().to_excel('样本2-相关系数.xlsx')

length = 11 # 最大可能的滞后
ans = np.zeros(length)
for i in range(length):
    ans[i] = df['[Al]'][i:].corr(df['[B]'][:-1-i])
#    print(ans[i])


plt.scatter(range(length),ans)
plt.plot(range(length),abs(ans))
plt.show()
