# -*- coding: utf-8 -*-
'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
class Ball():
    def __init__(self):   #初始化高度 100
        self.hight = 100
        
    def full(self):       # 球跌落了
        return self.hight # 返回本次跌落走过的路程
    
    def rebound(self):    # 球弹起来了
        self.hight = 0.5 * self.hight
        return self.hight # 返回本次弹起来走过的路程
        
b = Ball()                # 拿起一个球, 叫 b
route = 0
for i in range(9):       # 进行九次落下,并弹起来的实验
    route += b.full()
    route += b.rebound()    
        
route += b.full()  
print("第十次落地总路径: ", route)        
print("第十次反弹多高: ", b.rebound())        