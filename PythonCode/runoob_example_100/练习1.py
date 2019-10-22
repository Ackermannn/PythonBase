num = 0
for i in range(1,5):
    for  j in range(1,5):
        for  k in range(1,5):
            if ((i != j ) and (i!= k ) and (j != k )):
                print('互不相同且无重复数字的三位数: %d %d %d' %(i, j, k))
                num += 1
print('该三位数个数为：%d' % num)
