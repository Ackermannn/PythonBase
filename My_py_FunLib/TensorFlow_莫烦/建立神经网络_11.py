import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


# 制造数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]    # 加维度
noise = np.random.normal(0, 0.05, x_data.shape)    # 加噪点
y_data = np.square(x_data) - 0.5 + noise

# 隐藏层有十个神经元 输入层一个 输出层一个
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)   # 人们通常用的激励方程: tf.nn.relu 还有别的尝试
prediction = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(
            tf.reduce_sum(    # reduce_sum ~ sum
                tf.square(ys - prediction), reduction_indices=[1]    # 求方差
            )
        )
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # GradientDescentOptimizer里给学习率,且小于1

init = tf.initialize_all_variables()  # 初始化所有
sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
