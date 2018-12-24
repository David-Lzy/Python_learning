import tensorflow as tf
a = tf.constant([1.0,2.0],name='a')
b = tf.constant([2.0,2.0,],name='b')
g = tf.Graph()
with g.device('/gpu:0'):
result = a+b
sess = tf.Session()
sess.run(result)
print(result)