import os
import sys
import tensorflow as tf

Model_Path ='/opt/project/storage/models/mymodel.h5'


def load_models(config):
    model = tf.keras.models.load_model(Model_Path)