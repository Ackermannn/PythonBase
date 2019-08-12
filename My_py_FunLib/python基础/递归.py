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



