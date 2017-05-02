import tensorflow as tf

tf.InteractiveSession()

x = [[1,2,3], [4,5,6]]
y = [[7,8,9], [10,11,12]]

z = tf.concat([x,y], 0)
print(z.eval())

z = tf.concat([x,y], 1)
print(z.eval())

''' results
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
'''