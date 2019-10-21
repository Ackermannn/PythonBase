#https://www.bilibili.com/video/av16926522/?p=30
#莫烦python
import copy
a = [1,2,3]
b = a
id(a)
id(b)
b[0]=11
a[1]=22
b
print(id(a)==id(b))# True
c=copy.copy(a)
print(id(a)==id(c))# False

e = copy.deepcopy(a)
'''
直接 b = a 指针是指向同一块内存的,此时修改 a 时 b 连带改变
可以使用 b = a.copy()避免此种情况
