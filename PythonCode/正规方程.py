import numpy as np
A = np.array([[1,2104,5,1,45],
              [1,1416,3,2,40],
              [1,1534,3,2,30],
              [1,852,2,1,36]
              ])
y = np.array([460,232,315,178]).reshape((4,1))

temp = np.dot(A.T,A)
temp = np.linalg.inv(temp)
temp = np.dot(temp,A.T)
temp = np.dot(temp,y)
print(temp)
print(np.dot(A,temp),y)
