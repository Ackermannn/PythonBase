# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## 最速下降法
## 最优化程序实现 # 无约束寻极小值，适合求解凸函数

# 区间搜索
import numpy as np
def range_query(t0, func, h=1.0):
    if isinstance(t0, int): t0 = float(t0)
    if isinstance(h, int): h = float(h)
#    h = float(h)
    
    y0 = func(t0)
    t2 = t0 + h
    y2 = func(t2)
    
    if y2 >= y0: 
        t1 = t2
#        y1 = y2
        h = -1*h
    else:
        t1 = t0
#        y1 = y2
        t0 = t2
        y0 = y2
        h = 2*h
        
    for i in range(10000):

        try:
              
            t2 = t0 + h
            y2 = func(t2)  
        except OverflowError:
            print("数据溢出， 可能此函数没有极值")
            break
        
        if y2 > y0:
            a = min(t1, t2)
            b = max(t1, t2)
            return (a, b)
            break
        else:
            t1 = t0
#            y1 = y2
            t0 = t2
            y0 = y2
            h = 2*h
    raise RuntimeError('time out 可能函数没有极值, 你可以调节下步长，初始点')
# 黄金分割法
def golden_section(t0, func, **kwarg):
    '''
    t0： 初始点
    func: 目标函数
    h: 步长 
    e: 搜索精度，abs(t1 - t2) < e 时搜索结束
    '''
    h = 1.0 if not 'h' in kwarg else kwarg['h']
    e = 10e-5 if not 'e' in kwarg else kwarg['e']
    from math import sqrt
    beta = (sqrt(5) - 1) / 2
    a, b = range_query(t0, func, h)
    t2 = a + beta * (b - a)
    y2 = func(t2)
    t1 = a + b - t2
    y1 = func(t1)
    while (True):
        if (abs(t1 - t2) < e): return (t1 + t2) / 2
        if (y1 <= y2):
            b, t2, y2 = t2, t1, y1
            t1 = a + b - t2
            y1 = func(t1)
        else:
            a, t1, y1 = t1, t2, y2
            t2 = a + beta * (b - a)
            y2 = func(t2)

def steepest_descent(x0, func, dfunc, **kwarg):
    
    '''
    s_e 最速下降法的精度
    底层区间搜索的参数
    h: 步长 
    e: 搜索精度，abs(t1 - t2) < e 时搜索结束
    '''
    s_e = 10e-5 if not 's_e' in kwarg else kwarg['s_e']
    h = 1.0 if not 'h' in kwarg else kwarg['h']
    e = 10e-5 if not 'e' in kwarg else kwarg['e']
    y0 = func(x0)
    g0 = dfunc(x0)
    while (True):
        def funcls(t):
            return func(x0 - t * g0)

        t = golden_section(funcls(x0), funcls, h=h, e=e)
        x = x0 - t * g0
        y = func(x)
        g = dfunc(x)
        
        if (np.sum(g ** 2) < s_e):  # stop
            return x
        x0 = x
        y0 = y
        g0 = g

def func1(x):
    return -1*(1-x[0]**2-x[1]**2)

def dfunc1(x):
    x[0] =  2*x[0]
    x[1] =  2*x[0]
    return x

def fun2(x):
    return (x**2)**(1/3)-(x**2+1)**(1/3)

def fun3(x):
    return x**3 - x

x0 = np.array([12, 45], dtype=float)
x = steepest_descent(x0, func1, dfunc1, h=1)
print(x)
print("golden find the min value: {:.5f}".format(func1(x)))

#res = range_query(0.1, func1, h=1)
#print(res)  
#res = golden_section(0.1, func1)
#print("golden find: {:.5f}".format(res))
