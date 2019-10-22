# my origin way
```python
for i in range(1,10):
    str1 = ''
    for j in range(1,10):
        if i >= j:
            str0 = ( '%d * %d = %2d   '  % (i, j, i*j) )
            str1 = str1 + str0
    print(str1)
#input('输入任意键关闭程序')
```
# new way
```python
# -*- coding: UTF-8 -*-
for i in range(1,10):
    for j in range(1,i+1):
            print(' {}*{}={}'.format(i, j, i*j),end=',')
    print()

```
