"""
    It is one of the preprocessing components in which the image is rotated.
"""
import cv2
import os
import sys
import numpy as np
import tensorflow as tf
from PIL import Image


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
        print(self.request.data)
        self.request.model = PackageModel(**(self.request.data))

        self.image = self.request.get_param("inputImage")

        self.model = bootstrap["model"]


    @staticmethod
    def bootstrap(config: dict) -> dict:
        model=load_models(config=config)
        return model

    def predict_traffic_sign(img):
        return img

"""
    def predict_traffic_sign(img,model):

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

        try:
            # Görseli aç ve uygun boyuta getir
            image = img.resize((30, 30))
            image = np.array(image)

            # Modelin girdi formatına uygun hale getir
            image = np.expand_dims(image, axis=0)  # (1, 30, 30, 3) şekline getir
            '''
            image = image / 255.0  # Normalizasyon
            '''
            # Model ile tahmin yap
            predictions = model.predict(image)
            predicted_class = np.argmax(predictions) + 1  # En yüksek olasılığa sahip sınıfı al
            confidence = np.max(predictions)
            class_label = classes[predicted_class]

            image_to_draw = np.array(img)  # Orijinal boyut
            image_to_draw = cv2.cvtColor(image_to_draw, cv2.COLOR_RGB2BGR),cv2.putText(image_to_draw,
                f"{class_label} ({confidence:.2f})",
                org=(10, 25),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.7,
                color=(0, 255, 0),
                thickness=2
            )

            return classes[predicted_class], confidence
        except Exception as e:
            print(f"Hata oluştu: {e}")

            return image_to_draw
"""
    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.predict_traffic_sign(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_CatOrDog(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()