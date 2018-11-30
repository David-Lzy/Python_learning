import math
import scipy
import tensorflow 
import numpy 

#create some data
x_data = numpy.random.rand(1000).astype(numpy.float32)
y_data = x_data**2 + x_data*5 + (-1)

#create tensorflow structure start
Weights = tensorflow.Variable(tensorflow.random_uniform([1],-1.0,1.0))
biases = tensorflow.Variable(tensorflow.zeros([1]))

y = Weights*x_data + biases

loss = tensorflow.reduce_mean(tensorflow.square(y-y_data))
optimizer = tensorflow.train.GradientDescentOptimizer(0.05)
train = optimizer.minimize(loss)

init = tensorflow.global_variables_initializer()
#create tensorflow structure end

sess = tensorflow.Session
sess.run(init)

for step in range(500):
    sess.run(train)
    if step %20 == 0:
        print(step, sess.run(Weights), sess.run(biases))