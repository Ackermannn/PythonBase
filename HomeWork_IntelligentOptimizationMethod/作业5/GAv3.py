# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:23:22 2019

@author: Administrator
"""

# 变量类型为 0 - 15 的整数
import numpy as np
import time
start = time.clock()
value = np.array([28, 16, 24, 18, 22, 6, 14, 0, 20, 12, 10, 2, 8, 4, 6, 30])

def DF(input0): # x为np向量
    return np.sum(value[input0])

print(DF(np.array([0,5,6])))
    
gene_len = 25
popu_size = 500  # 种群数量 最好是偶数
pc = 0.90  # 交叉概率
pm = 0.002  # 变异概率   

population = np.random.randint(0,16,size=(popu_size, gene_len))    
max_fitness = 0
max_g = None

for ii in range(1000):
    fitness = np.array([DF(population[i]) for i in range(popu_size)])
    temp = np.max(fitness)
    if temp >= max_fitness:
        max_fitness = np.max(fitness)
        max_g = population[fitness.argmax()]    
    print("迭代: ",ii," 最大适应度: ", temp,"  历史: ",max_fitness)
    
    # 选择
    choice_probility = fitness / np.sum(fitness)
    accumulate_probility = np.cumsum(choice_probility)
    
    # 轮盘赌
    chp = np.random.rand(popu_size)
    new_population = np.zeros((popu_size, gene_len),dtype=int)
    for j, r in enumerate(chp):
        for i, p in enumerate(accumulate_probility):
            if i == 0 and r < p:
                new_population[j] = population[i].copy()
            else:
                if r < p and r >= accumulate_probility[i - 1]:
                    new_population[j] = population[i].copy()
                    
    if all([all(population[:,i] == population[0,i]) for i in range(gene_len)]): break
    
    half = int(popu_size / 2)
    chp = np.random.rand(half)
    for i,p in enumerate(chp):
        if p < pc:
            ch1,ch2 =np.random.randint(1, gene_len,2)
            ch1, ch2 = min(ch1,ch2), max(ch1, ch2)
            new_population[i][ch1:ch2], new_population[i + half][ch1:ch2] = \
                new_population[i + half][ch1:ch2].copy(), new_population[i][ch1:ch2].copy()
                
    # 变异
    chp = np.random.rand(popu_size, gene_len)
    for i,chro in enumerate(new_population):
        for j,gm in enumerate(chro):
            if chp[i,j] < pm:
                new_population[i][j] = np.random.randint(0,16)
    
    
    population = new_population.copy()
    
print("历史最大适应度: ", max_fitness)
print("他的染色体是: ", max_g)
print(max_fitness/750, "找到1111的片段数",sum(max_g==15),"/ 25")
elapsed = (time.clock() - start)
print("Time used:",elapsed)    
    
'''
历史最大适应度:  738
他的染色体是:  [15 15  0 15 15  2 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15  0
  0]
0.984 找到1111的片段数 21 / 25
Time used: 126.736212
'''
    
