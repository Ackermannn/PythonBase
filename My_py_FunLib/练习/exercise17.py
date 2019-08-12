a = input('请输入一串字符:')  # python 3 支持中文做变量
英文 = 0
空格= 0
数字= 0
其他= 0
for i in a:
    if i.isalpha():
        英文 += 1
    elif i.isspace():
        空格 += 1
    elif i.isnumeric():
        数字 += 1
    else:
        其他 += 1
print('英文 = %s,空格 = %s,数字 = %s,其他 = %s' % (英文,空格,数字,其他))
