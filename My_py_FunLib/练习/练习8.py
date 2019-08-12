for i in range(1,10):
    str1 = ''
    for j in range(1,10):
        if i >= j:
            str0 = ( '%d * %d = %2d   '  % (i, j, i*j) )
            str1 = str1 + str0
    print(str1)
#input('输入任意键关闭程序')
