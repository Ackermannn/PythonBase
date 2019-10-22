import numpy as np
A = np.array([1,1,1])
print(A.shape)
A2 = A.reshape(1,A.shape[0])
print(A2.shape)
