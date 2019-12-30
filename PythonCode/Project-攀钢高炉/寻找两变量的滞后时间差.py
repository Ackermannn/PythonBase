import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def late_analysis(df, length):
    '''
    df: 输入的 DataFrame 类数据
    length: 给出最大可能的滞后
    
    画时滞图
    '''
    ans = np.zeros(length)
    ans[0] = df[0].corr(df[1])
    for i in range(1,length):
        df2 = pd.DataFrame([np.array(df[0][i:]), np.array(df[1][:-1*i])]).T
        ans[i] = df2.corr()[0][1]
    
    
    plt.figure()
    plt.plot(range(length),abs(ans))
    plt.show()


x0 = np.arange(0,2*np.pi,0.1)
x0 = np.sin(x0)

x1 = np.arange(0+0.5,2*np.pi+0.5,0.1)
x1 = np.sin(x1)
plt.plot(x0)
plt.plot(x1)
length = 40 # 给出最大可能的滞后
df = pd.DataFrame(data=[x0,x1]).T 
late_analysis(df, length)