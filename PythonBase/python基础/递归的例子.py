#========斐波那契数列============
'''
def fib(month):
    
    if month == 1 or month == 2:
        return 1
    else:
        return fib(month-1) + fib(month-2)

print('斐波那契数列的兔子经历了几个月了？')
month = int(input())
print('哇，已经有了%d个兔子了' % fib(month))
'''
'''
分治思想
'''
#运行很慢......
'''
'''

def hano(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        hano(n-1, x, z, y)
        print(x, '->', z)
        hano(n-1, y, x, z)
        
print('汉诺塔有多少层呀')
n = int(input())
hano(n,'x','y','z')
