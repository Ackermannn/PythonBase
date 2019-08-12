# zip用法
a = [1,2,3]
b = [4,5,6]
zip(a,b)
list(zip(a,b)) #可视化zip(a,b)是什么
# 打印 [(1,4),(2,5),(3,6)]

#可以这样配合for循环
for i,j in zip(a,b)
    print(i/2,j*2)

zip(a,a,b)#可以合并更多元素

#### lambda用法 #######
fun2 = lambda x,y:x+y
fun2(2,3)

#### map用法 ####
def fun1(x,y)
    return (x,y)
list(map(fun1,[1,2],[2,5]))
# 返回 [3,8]
'''
from bilibili 莫烦
'''
