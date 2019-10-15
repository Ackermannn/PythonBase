# -*- coding: utf-8 -*-
import numpy as np


def DF4(str4):
    value = [28, 16, 24, 18, 22, 6, 14, 0, 20, 12, 10, 2, 8, 4, 6, 30]
    idx = int(str4, 2)
    return value[idx]


def DF100(str100):
    return sum([DF4(str100[i: i + 4]) for i in range(0, gmlen, 4)])


popu_size = 100  # 种群数量 最好是偶数
pc = 0.9  # 交叉概率
pm = 0.05  # 变异概率
gmlen = 4 * 25
# 种群初始化
numlist = list(np.random.randint(0, 2, size=(popu_size, gmlen)))
population = ["".join([str(x) for x in numlist[i]]) for i in range(popu_size)]

max_fitness = 0
max_g = ""
for ii in range(300):
    # 计算适应度
    fitness = np.array([DF100(population[i]) for i in range(popu_size)])
    # 储存历史极大
    if max(fitness) >= max_fitness:
        max_fitness = max(fitness)
        max_g = population[fitness.argmax()]
        
    print("迭代: ",ii+1," 最大适应度: ",max(fitness))
    
    # 选择
    choice_probility = fitness / sum(fitness)
    accumulate_probility = np.cumsum(choice_probility)
    # 轮盘赌
    randnum = np.random.rand(popu_size)
    new_population = []
    for r in randnum:
        for i, p in enumerate(accumulate_probility):
            if i == 0 and r < p:
                new_population.append(population[i])
            else:
                if r < p and r >= accumulate_probility[i - 1]:
                    new_population.append(population[i])
    # 交叉
    half = int(popu_size / 2)
    for i,chro1 in enumerate(new_population[:half]):
        if np.random.rand() < pc:
            ch = np.random.randint(1, gmlen)
            chro2 = new_population[i + half]
            chro1, chro2 = chro1[:ch] + chro2[ch:], chro2[:ch] + chro1[ch:]
            new_population[i], new_population[i + half] = chro1, chro2
    # 变异
    for chro in new_population:
        for gm in chro:
            if np.random.rand() < pm:
                gm = str(1 - int(gm))
    population = new_population.copy()
print("历史最大适应度: ", max_fitness)
print("他的染色体是: ", max_g)
print(max_fitness/750)
# 跑出来的结果在600以上 甚至到650 ,最好是750
