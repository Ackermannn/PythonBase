#=====while 与 else 的配合


def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d最大的约数是%d' % (num,count))
            break  # 如果没有break 就跑else
        count -= 1
    else:
        print('%d是素数！' % num)

num = int(input('请输入一个数：'))
showMaxFactor(num)

# try 可以与 else 配合

# 简洁的with的语句

try:
    with open('data.txt','w') as f  #?????????
    for each_line in f
        print(each_line)
except OSError as reason
    print('出错了'+str(reason))

