import os
import sys
import tensorflow as tf

Model_Path = "/storage/models/mymodel.h5"


def load_models(config):
    if not os.path.exists(Model_Path):
        raise FileNotFoundError(f"Model dosyası bulunamadı: {Model_Path}")

    try:
        model = tf.keras.models.load_model(Model_Path)
        if model is None:
            raise ValueError("Model yüklenemedi, 'None' döndü!")
        return model
    except Exception as e:
        print(f"Model yüklenirken hata oluştu: {e}")
        raise
