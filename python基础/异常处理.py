#====异常处理============================================
try:
    f = open('我为啥是个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错率 \n错误的原因是：'+ str(reason))
except TypeError as reason:
    print('类型出错率 \n错误的原因是：'+ str(reason))

#except (TypeError,OSError)


    
#===如果不知道哪里错了====不推荐===
try:
    f = open('我为啥是个文件.txt')
    print(f.read())
    f.close()
except:
    print('出错了T_T')


#============================
try:
    #检测范围
except:
    #异常处理
finally:
    #无论如何都会执行

#===============
# 关键字
# raise
