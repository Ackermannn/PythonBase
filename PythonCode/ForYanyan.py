def ptintLine(w1,s1,w2,s2):
    str1 = ""
    for i in range(w1):
        str1 += " "
    for i in range(s1):
        str1 += "*"
    for i in range(w2):
        str1 += " "
    for i in range(s2):
        str1 += "*"
    print(str1)
ptintLine(4,4,12,4)
ptintLine(2,8,8,8)
ptintLine(0,12,4,12)
for i in range(4):
    ptintLine(i,28-2*i,0,0)
for i,j in zip([6, 9, 12],[16,10,4]):
    ptintLine(i,j,0,0)
ptintLine(13,2,0,0)
input("输入任意字符终止程序")
