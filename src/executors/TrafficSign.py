"""
    It is one of the preprocessing components in which the image is rotated.
"""
import cv2
import os
import sys
import numpy as np
import tensorflow as tf


sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.MScaling.src.utils.response import build_response_TraficSign
from components.MScaling.src.models.PackageModel import PackageModel
from components.MScaling.src.utils.utils import load_modelstwo


class TrafficSign(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        #print(self.request.data)
        self.request.model = PackageModel(**(self.request.data))

        self.image = self.request.get_param("inputImage")
        #print("image:",self.image)
        self.show = self.request.get_param("Show")
        self.model = bootstrap["model"]
        print("model:",self.model)



    @staticmethod
    def bootstrap(config: dict) -> dict:
        model = load_modelstwo(config=config)
        return {"model":model}

    def Put(self,img):

        if self.show == "ShowText":
            self.show="Merhaba"
        else:
            self.show="100"

        text =self.show

        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)

        h,w,_ = img.shape[2]

        h=w - text_width - 10
        w = 30

        color = (0, 255, 0)
        cv2.putText(
            img,
            text,
            (h, w),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2,
            cv2.LINE_AA
        )

        return img

    def predict_and_annotate(self,img):
        """
        Görsel üzerinde tahmin yapar, sonucu sol üst köşeye yazar ve resmi döndürür.
        """

        import numpy as np
        import tensorflow as tf
        from tensorflow.keras.models import load_model
        from PIL import Image



        classes = {
            1: 'Speed limit (20km/h)', 2: 'Speed limit (30km/h)', 3: 'Speed limit (50km/h)',
            4: 'Speed limit (60km/h)', 5: 'Speed limit (70km/h)', 6: 'Speed limit (80km/h)',
            7: 'End of speed limit (80km/h)', 8: 'Speed limit (100km/h)', 9: 'Speed limit (120km/h)',
            10: 'No passing', 11: 'No passing veh over 3.5 tons', 12: 'Right-of-way at intersection',
            13: 'Priority road', 14: 'Yield', 15: 'Stop', 16: 'No vehicles', 17: 'Veh > 3.5 tons prohibited',
            18: 'No entry', 19: 'General caution', 20: 'Dangerous curve left', 21: 'Dangerous curve right',
            22: 'Double curve', 23: 'Bumpy road', 24: 'Slippery road', 25: 'Road narrows on the right',
            26: 'Road work', 27: 'Traffic signals', 28: 'Pedestrians', 29: 'Children crossing',
            30: 'Bicycles crossing', 31: 'Beware of ice/snow', 32: 'Wild animals crossing',
            33: 'End speed + passing limits', 34: 'Turn right ahead', 35: 'Turn left ahead',
            36: 'Ahead only', 37: 'Go straight or right', 38: 'Go straight or left', 39: 'Keep right',
            40: 'Keep left', 41: 'Roundabout mandatory', 42: 'End of no passing', 43: 'End no passing veh > 3.5 tons'
        }

        if isinstance(img, np.ndarray):
            # Float tipindeyse uint8'e çevir ve PIL image oluştur
            img_uint8 = img.astype(np.uint8)
            pil_image = Image.fromarray(img_uint8)
        else:
            raise ValueError("Giriş sadece NumPy array (img) olmalı")

        image = pil_image.resize((30, 30))
        #image = np.array(image).astype(np.float32) / 255.0
        image = np.expand_dims(image, axis=0)

        predictions = self.model.predict(image)
        predicted_class = np.argmax(predictions) + 1
        confidence = np.max(predictions)

        text = f"{classes[predicted_class]} ({confidence:.4f})"

        color = (0, 255, 0)
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
        img.value = self.Put(img.value, self.show)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_TraficSign(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()