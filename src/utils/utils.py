import os
import sys
import tensorflow as tf

Model_Path ='F8877E/storage/models/mymodel.h5'


def load_models(config):
    model = tf.keras.models.load_model(Model_Path)