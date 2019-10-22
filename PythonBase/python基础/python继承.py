import random as r

class Fish:#这里类定义冒号结尾

    def __init__(self):#这里方法定义也要冒号结尾
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
       # self.y -= 1
        print('我的位置是：',self.x,self.y)
    
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):

    def __init__(self):
        self.hungry = True
        super().__init__()#  super 继承  如果被覆盖掉了
      #  Fish.__init__(self)
        
    def eat(self):
        if self.hungry:#冒号
            print('吃货的梦想就是天天有的吃^_^')
            self.hungry = False
        else:#冒号
            print('太撑了，吃不下了！')
'''
多重继承 尽量不要使用
'''
