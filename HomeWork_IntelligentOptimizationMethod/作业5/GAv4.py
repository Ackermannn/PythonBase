# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:53:43 2019

@author: Ackerman

last edited on Thu Oct 17 13:15:43 2019 
"""
import numpy as np
import time

start = time.clock()
# const setting
DF_VALUE = np.array([28, 16, 24, 18, 22, 6, 14, 0, 20, 12, 10, 2, 8, 4, 6, 30])
R = 0.9         # 标定系数r
M = 1000        # 标定系数M
GENE_LEN = 25   # 染色体长度
POP_SIZE = 100  # 种群数量 最好是偶数
PC = 0.90  # 交叉概率
PM = 0.01 # 变异概率 


class GA:
    
    
    def __init__(self):
        # 初始化
        self.sigma = M 
        self.population = np.random.randint(0,16,size=(POP_SIZE, GENE_LEN))    
        self.max_fitness = 0
        self.max_g = None


    def DF(self, input0): # x为np向量
        
        return np.sum(DF_VALUE[input0])
    
    
    def cal_value(self):
        
        self.value = np.array([self.DF(self.population[i]) for i in range(POP_SIZE)])
        temp = np.max(self.value)
        if temp >= self.max_fitness:
            self.max_fitness = np.max(self.value)
            self.max_g = self.population[self.value.argmax()]


    def calibrate(self):## 动态线性标定参数
        
        self.fitness = self.value - np.min(self.value) + self.sigma
        self.sigma *= R


    def roulette(self):
    
        choice_probility = self.fitness / np.sum(self.fitness)
        accumulate_probility = np.cumsum(choice_probility)
    
        chp = np.random.rand(POP_SIZE)
        self.new_population = np.zeros((POP_SIZE, GENE_LEN),dtype=int)
        for j, k in enumerate(chp):
            for i, p in enumerate(accumulate_probility):
                if i == 0 and k < p:
                    self.new_population[j] = self.population[i]
                else:
                    if k < p and k >= accumulate_probility[i - 1]:
                        self.new_population[j] = self.population[i] 


    def cross(self):
        
        half = int(POP_SIZE / 2)
        chp = np.random.rand(half)
        for i,p in enumerate(chp):
            if p < PC:
                ch1,ch2 =np.random.randint(1, GENE_LEN, 2)
                ch1, ch2 = min(ch1,ch2), max(ch1, ch2)
                self.new_population[i][ch1:ch2], self.new_population[i + half][ch1:ch2] = \
                    self.new_population[i + half][ch1:ch2].copy(), self.new_population[i][ch1:ch2].copy()
    
    
    def variate(self):
        
        chp = np.random.rand(POP_SIZE, GENE_LEN)
        for i,chro in enumerate(self.new_population):
            for j,gm in enumerate(chro):
                if chp[i,j] < PM:
                    self.new_population[i][j] = np.random.randint(0,16)
        self.population = self.new_population.copy()
    
    

g = GA()
for ii in range(1000):
    g.cal_value()
    print("迭代: ",ii," 最大适应度: ", np.max(g.value),"  历史: ",g.max_fitness)
    if np.max(g.value) == 750: break
    g.calibrate() # 动态线性标定
    g.roulette() # 轮盘赌
    g.cross()   # 交叉
    g.variate() # 变异
    
print("历史最大适应度: ", g.max_fitness)
print("他的染色体是: ", g.max_g)
print(g.max_fitness/750, "找到1111的片段数",sum(g.max_g==15),"/ 25")

elapsed = (time.clock() - start)
print("Time used:",elapsed)    
    
