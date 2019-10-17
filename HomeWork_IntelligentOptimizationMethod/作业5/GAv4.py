# -*- coding: utf-8 -*-
# 写个class
# 变量类型为 0 - 15 的整数
import numpy as np
import time

start = time.clock()

class GA:
    
    df_value = np.array([28, 16, 24, 18, 22, 6, 14, 0, 20, 12, 10, 2, 8, 4, 6, 30])
    r = 0.9
    gene_len = 25
    popu_size = 100  # 种群数量 最好是偶数
    pc = 0.90  # 交叉概率
    pm = 0.01 # 变异概率 
    
    def __init__(self):
        # 初始化
        self.sigma = 1000 
        self.population = np.random.randint(0,16,size=(GA.popu_size, GA.gene_len))    
        self.max_fitness = 0
        self.max_g = None

    def DF(self, input0): # x为np向量
        return np.sum(GA.df_value[input0])
    
    
    def cal_value(self):
        self.value = np.array([self.DF(self.population[i]) for i in range(GA.popu_size)])
        temp = np.max(self.value)
        if temp >= self.max_fitness:
            self.max_fitness = np.max(self.value)
            self.max_g = self.population[self.value.argmax()]


    def calibrate(self):## 动态线性标定参数
        self.fitness = self.value - np.min(self.value) + self.sigma
        self.sigma *= GA.r


    def roulette(self):
        choice_probility = self.fitness / np.sum(self.fitness)
        accumulate_probility = np.cumsum(choice_probility)
    
        chp = np.random.rand(GA.popu_size)
        self.new_population = np.zeros((GA.popu_size, GA.gene_len),dtype=int)
        for j, k in enumerate(chp):
            for i, p in enumerate(accumulate_probility):
                if i == 0 and k < p:
                    self.new_population[j] = self.population[i]
                else:
                    if k < p and k >= accumulate_probility[i - 1]:
                        self.new_population[j] = self.population[i] 


    def cross(self):
        half = int(GA.popu_size / 2)
        chp = np.random.rand(half)
        for i,p in enumerate(chp):
            if p < GA.pc:
                ch1,ch2 =np.random.randint(1, GA.gene_len,2)
                ch1, ch2 = min(ch1,ch2), max(ch1, ch2)
                self.new_population[i][ch1:ch2], self.new_population[i + half][ch1:ch2] = \
                    self.new_population[i + half][ch1:ch2].copy(), self.new_population[i][ch1:ch2].copy()
    
    
    def variate(self):
        chp = np.random.rand(GA.popu_size, GA.gene_len)
        for i,chro in enumerate(self.new_population):
            for j,gm in enumerate(chro):
                if chp[i,j] < GA.pm:
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
    
    
