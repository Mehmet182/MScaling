"""
    It is one of the preprocessing components in which the image is rotated.
"""
import cv2
import os
import sys
import numpy as np


sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.MScaling.src.utils.response import build_response_CatOrDog
from components.MScaling.src.models.PackageModel import PackageModel
from components.MScaling.src.utils.utils import load_models


class CatOrDog(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        #print(self.request.data)
        self.request.model = PackageModel(**(self.request.data))

        self.image = self.request.get_param("inputImage")
        #print("image:",self.image)

        self.model = bootstrap["model"]
        print("model:",self.model)



    @staticmethod
    def bootstrap(config: dict) -> dict:
        model = load_models(config=config)
        return {"model":model}


    def predict_and_annotate(self,img):
        """
        Görsel üzerinde tahmin yapar, sonucu sol üst köşeye yazar ve resmi döndürür.
        """

        from tensorflow.keras.preprocessing import image
        import tensorflow as tf

        img_resized = cv2.resize(img, (224, 224))
        img_array = image.img_to_array(img_resized) // 255.0
        img_array = tf.expand_dims(img_array, 0)

        prediction = self.model.predict(img_array)[0][0]

        if prediction > 0.5:
            #print("Tahmin: Köpek (%0.2f)" % prediction)
            label = "Köpek"
            confidence =prediction

        else:
            # print("Tahmin: Kedi (%0.2f)" % (1 - prediction))
            label = "Kedi"
            confidence = (1 - prediction)

        text = f"{label} ({confidence:.2f})"

        color = (0, 255, 0) if label == "Köpek" else (255, 0, 0)
        cv2.putText(
            img,
            text,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2,
            cv2.LINE_AA
        )

        return img



    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.predict_and_annotate(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_CatOrDog(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()