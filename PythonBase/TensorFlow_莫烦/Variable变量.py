import tensorflow as tf

state = tf.Variable(0, name='counter')  # 定义变量
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)  # new_value 赋值给 state

#  最重要的一步
init = tf.global_variables_initializer()  # 初始化所有变量 must have if define variable

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))   # 直接 print(state)是没有用的 必须sess.run()

