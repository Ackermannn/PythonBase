#===========字典================
'''
dict1 = {'李宁':'1231','xxx':'123126'} #创建字典 #标志性花括号
print('xxxxx:',dict1['李宁'])
dict1['爱迪生'] = '123131' #加入新的



'''
'''
dict1 = {}
dict1.fromkeys((1,2,3))
dict1.formkeys((1,2,3),'number')   # 只能创建新的字典
dict1 = dict1.fromkeys(range(32),'赞')
for each in dict1.keys():
    print(eachKey)

for each in dict1.values():
    print(eachKey)

for each in dict1.items():
    print(each)

'''
#----------get方法---------
'''
dict1.get(32,'木有')  返回 一个None
'''

# ------查看31 是否在dict1-------
'''
31 in dict1  
'''




#-----------如果dict1 赋值给 dict2了 执行时 全部清楚-------------
'''
dict1.clear() 
'''



# ------.copy 与 赋值 不同-------------
# P27

'''

>>> a = [1,2,3,4]
>>> b = a
>>> b
[1, 2, 3, 4]
>>> c = a.copy()
>>> a.append(999)
>>> a
[1, 2, 3, 4, 999]
>>> b
[1, 2, 3, 4, 999]
>>> c
[1, 2, 3, 4]

'''


# dict1.pop(2)
# dict1.popitem() 随机pop













