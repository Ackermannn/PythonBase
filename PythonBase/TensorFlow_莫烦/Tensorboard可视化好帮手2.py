import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):

        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name+'/weights', Weights)

        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)

        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)

        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
            tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs


# 制造数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]    # 加维度
noise = np.random.normal(0, 0.05, x_data.shape)    # 加噪点
y_data = np.square(x_data) - 0.5 + noise

# 隐藏层有十个神经元 输入层一个 输出层一个


with tf.name_scope('input'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')  # 起名字
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# 加入隐藏层
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)   # 人们通常用的激励方程: tf.nn.relu 还有别的尝试
# add  output layer
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(
                tf.reduce_sum(    # reduce_sum ~ sum
                    tf.square(ys - prediction), reduction_indices=[1]    # 求方差
                )
            )
    tf.summary.scalar('loss', loss)
# 训练
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # GradientDescentOptimizer里给学习率,且小于1

# 初始化所有
init = tf.initialize_all_variables()

# 启动对话框
sess = tf.Session()
sess.run(init)
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('logs/', sess.graph)


for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        result = sess.run(merged,
                          feed_dict={xs: x_data, ys: y_data})
        writer.add_summary(result, i)
        #print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))



# 再在控制台 输入 tensorboard --logdir=D:\anaconda3\envs\MyEnvironment\Tensorflow\logs
# logdir= 是tf.summary.FileWriter的存放路径
# 再在浏览器输入 localhost:6006 或者 cmd 输出的网址即可欣赏TensorBoard , 开着黑框才能打开
