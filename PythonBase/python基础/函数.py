# ===========函数===========
'''
def MyFirstFunction():
    '函数文档' # help(MyFirstFunction)可查看
    print('12345679')
    print('45679')
'''
# SaySome(word = '',name = '') 关键字参数

# def SaySome(word = '',name = '') 默认值  参数设置默认值



# =============收集参数==============
'''
def test(*params,exp = 0)  # 收集参数
    print('参数的长度：',len(params),exp);
    print('第二个参数是：',params[1]);
'''

# =========返回多个值-----python 更灵活=======
'''
def back():
    return [1,'xiajiayu',3.14]
'''
#子函数可以访问全局变量，不可以修改全局变量

#===========内嵌函数与闭包==============
'''
global 关键字

python支持函数嵌套


'''
####========闭包================
'''
def FunX(x):
    def FunY(y):
        return x * y
    return FunY   #万物皆对象

>>>i = FunX(8)
>>>i

>>>type(i)
>>>i(5)
>>>FunX(8)(5)




'关键字 nonlocal'

'''
#=========== 匿名函数==========
'''
g = lambda x, y : x + y
>>>g(3,4)
'''

#===========两个牛逼的BIF========
'''
filter(None,[1,0,False,True])
list(filter(None,[1,0,False,True]))  ->  [1,True]

list(filter(lambda x: x % 2 ,range(10)))

map 用法

'''

#============== 递归==================
# 递归深度默认100层 可修改


# 传统版本
'''
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
 


number = input('请输入一个整数:')
number = int(number)
result = factorial(number)
print('%d的阶乘是:%d' % (number,result))
'''


#递归版本

def factorial(n):
    if n == 1:
        return 1                    # 有停止条件
    else:
        return n * factorial(n-1)   # 调用自身

number = input('请输入一个整数:')
number = int(number)
result = factorial(number)
print('%d的阶乘是:%d' % (number,result))











