import numpy as np
A = np.array([[3,1,1,1],
              [1,3,1,1],
              [1,1,3,1],
              [1,1,1,3]])
B = np.array([[1,1,1,1],
              [1,3,1,1],
              [1,1,3,1],
              [1,1,1,3]])
##a = round(np.linalg.det(A))
##b = round(6 * np.linalg.det(B))
##print(a == b)

if (np.linalg.det(A) - 6 * np.linalg.det(B)) < 1e-1:
    print('True')
else:
    print('False')
'''
|3 1 1 1|          |1 1 1 1|   
|1 3 1 1|   =  6 * |1 3 1 1|
|1 1 3 1|          |1 1 3 1|
|1 1 1 3|          |1 1 1 3|
'''
