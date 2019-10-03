# -*- coding: utf-8 -*-
"""
@author: Ackerman

Last eidt on Oct 3 13:16:00 2019
"""
import numpy as np
from scipy import stats

def getTotalTime(utility, plan):
    return np.sum(utility[list(range(100)),plan])


def hillClimb(utility, plan):
    historyMinTime = np.inf
    for j in range(150):
        NerMinTime = historyMinTime  # 寻找邻域最小
        NerMinplan = plan.copy()
        innerLoop = 100
        for i in range(innerLoop):
        #    lp +=1
            idx1, idx2 = np.random.randint(low = 0, high = 100,size = (2,))
            ch_plan = plan.copy()
            ch_plan[idx1], ch_plan[idx2] = ch_plan[idx2], ch_plan[idx1]
            temp = getTotalTime(utility, ch_plan)
    
            if temp <= NerMinTime:
                NerMinTime = temp.copy()
                NerMinplan = ch_plan.copy()
                
        if NerMinTime < historyMinTime:
            plan = NerMinplan.copy()     
            historyMinTime = NerMinTime.copy()
        else:
            break  
    return historyMinTime

def SA(utility, plan):
    historyMinTime = np.inf

    T = 100.0 # 温度初始化
    min_time = historyMinTime # 暂存初始化
    innerLoop = 100
    #lp = 0
    while T > 0.1:
        for i in range(innerLoop):
        #    lp +=1
            idx1, idx2 = np.random.randint(low = 0, high = 100,size = (2,))
            plan[idx1], plan[idx2] = plan[idx2], plan[idx1]
            temp = getTotalTime(utility, plan)
            if temp <= min_time:
                min_time = temp.copy() #   无条件转移
               # print("无条件转: ",min_time)
                if temp < historyMinTime: 
                    historyMinTime = temp.copy()
                    #print("历史最小: ",historyMinTime)
            else:
                proility = np.exp((temp - min_time)/(-T))
                if np.random.rand() < proility:
                    min_time = temp.copy()
                    #print("概率接受: ",min_time)
                else:
                    plan[idx1], plan[idx2] = plan[idx2], plan[idx1]
           # if  lp % 5000 == 1:print("此时历史最小: ",historyMinTime)
        T *= 0.9  
    return historyMinTime

res2 = [];res1 = []
for i in range(30):
    utility = np.random.randint(low = 1, high = 101, size = (100,100))  # 100 * 100 的矩阵 数值从[1,100]中随机取 
    plan = np.arange(100)
    np.random.shuffle(plan)
    res1.append(hillClimb(utility, plan))
    print("爬山的最小: ",res1[-1])  
    res2.append(SA(utility, plan))
    print("SA的最小: ", res2[-1])
if stats.ttest_ind(res1,res2,equal_var=False).pvalue < 0.05:
    print("两方法有显著差异")
