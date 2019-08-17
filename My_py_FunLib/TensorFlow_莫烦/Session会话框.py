import tensorflow as tf
import warnings

matrix1 = tf.constant([[3,3]])  # 常量
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1 , matrix2) # 矩阵乘法  np.dot(m1,m2)

#method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close() # 可有可无

#method 2  Session的两种打开模式
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result)


