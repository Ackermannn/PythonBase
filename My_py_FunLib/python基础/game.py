import random
secret = random.randint(1,10)

print("--------我的python游戏----------")
temp = 0
guess_number = 3
guess = int(temp)
#-----------------------------------------------------------------------------
while guess != secret and guess_number > 0:
    temp =input('从1到10的整数猜一个数（你有三次机会）:')
    
    guess = int(temp)
    if guess == secret:
        print('哇，你是怎么猜到的？')
        print('你赢了！！！WoW')
    else:
        guess_number = guess_number - 1
        if guess < secret:
            print("你猜小了")
        else:
            print("你猜大了")
    
#-----------------------------------------------------------------------------  
if guess_number == 0:
    print('你三次都没有猜对') 
print('游戏结束！')



'''
    BIF == Built-in function 内置函数
    dir(__builtins__) BIF有哪些
    help(input)
------------------------------------------
    str = r'C:\now' 原始字符串

    True and False 逻辑 and
------------------------------------------
    import random 导入random模块
    random模块 randint()返回整数
------------------------------------------
    类型转换
    int()
    str()
    float()
    type() 输出类型
    isinstance()
        isinstance(123,int) 返回True
------------------------------------------
    函数名不要和变量名重名
------------------------------------------
    a = a + 1 可以写成 a += 1
------------------------------------------
    // 地板除法      3.0 // 2 成了 1.0
    % 取余数
    ** 幂运算 3**2 意思3^2
------------------------------------------
    逻辑操作符 and or not
------------------------------------------
    优先级 幂运算**，正负号+，算术*/，比较，逻辑

------------------------------------------

elif 就是 else if

条件表达式 三元操作符 samll = x if x < y else y

assert 断言  assert 3 > 4  检查点

for 目标 in  
    循环
    
'''
