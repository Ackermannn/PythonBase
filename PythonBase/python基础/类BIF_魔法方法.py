'''
class C:
    def x(self):
        print('X-man!')
'''

'''
c = C()
c.x()

c.x = 1# 方法会被覆盖掉

# 方法用动词定义
# 属性用名词定义
'''

#绑定概念。。。。
#多使用实例化 

#======相关BIF============================
# https://www.bilibili.com/video/av4050443/?p=41
# issubclass( , ) # 子类检查   object基类
# isinstance( , ) # 实例检查
# hasattr(object, name) # hassattr(c1,'x')
    # getattr
    # setattr
    # delattr
# property(获取属性的方法，设置属性的方法，删除属性的方法 )


## =======魔法方法==========================
'''
__init__(self[,...])  ## 不要在__init__返回
__new__(cls[,...]) # 极少重写
__del__(self) # 不懂
'''
'''
----------算术的魔法方法---------------------
__add__
__sub__
__mul__等等
'''

