import numpy as np

A = np.arange(3,15).reshape((3,4))
A = np.random.randint(10,size=(3,4))
print('A=\n',A)
print('A[1]=\n',A[1])
print('A[2,1]=\n',A[2,1])
print('A[2][1]=\n',A[2][1])


print('A[1,1:4]=\n',A[1,1:4])

print('行迭代')
for column in A:
    print(column)
    
print('列迭代')
for column in A.T:
    print(column)

print('逐个迭代')
for item in A.flat:
    print(item)
