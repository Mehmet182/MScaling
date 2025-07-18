import os
import sys
import tensorflow as tf

Model_Path = "/storage/models/mymodel.h5"
Model_Pathtwo = "/storage/models/Trafic_signs_model.h5"


def load_models(config):
    if not os.path.exists(Model_Path):
        raise FileNotFoundError(f"CatOrDog Model dosyası bulunamadı: {Model_Path}")

    try:
        model = tf.keras.models.load_model(Model_Path)
        if model is None:
            raise ValueError("CatOrDog Model yüklenemedi, 'None' döndü!")
        return model
    except Exception as e:
        print(f"CatOrDog Model yüklenirken hata oluştu: {e}")
        raise



def load_modelstwo(config):
    if not os.path.exists(Model_Pathtwo):
        raise FileNotFoundError(f" Traffic Sign Model dosyası bulunamadı: {Model_Pathtwo}")

    try:
        model = tf.keras.models.load_model(Model_Pathtwo)
        if model is None:
            raise ValueError("Traffic Sign Model yüklenemedi, 'None' döndü!")
        return model
    except Exception as e:
        print(f"Traffic Sign Model yüklenirken hata oluştu: {e}")
        raise