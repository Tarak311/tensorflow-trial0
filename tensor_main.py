#!/usr/bin/python
import tensorflow as tf
model =tf.keras.Sequential()
model.add(tf.keras.layers.Dense(512.activation=tf.nn.relu, input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
