"""
    It is one of the preprocessing components in which the image is rotated.
"""
import cv2
import os
import sys
import numpy as np
# from PIL import Image


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
        model = load_models(config=config)
        return {"model": model}

    def predict_and_annotate(img, model, image_size=(224, 224)):
        """
        Verilen model ve görsel üzerinde tahmin yapar, sonucu sol üst köşeye yazar ve resmi döndürür.

        Args:
            img: NumPy array formatında (BGR veya RGB) bir görüntü.
            model: Eğitilmiş TensorFlow/Keras modeli.
            image_size: Modele giriş için yeniden boyutlandırılacak hedef boyut.

        Returns:
            Annotated image (girdi ile aynı formatta, yazı yazılmış haliyle).
        """
        if img is None:
            raise ValueError("Geçersiz görüntü: img NoneType.")

        # Orijinal görüntüyü kopyala
        annotated_img = img.copy()

        # RGB'ye çevir (model genelde RGB bekler)
        if len(img.shape) == 3 and img.shape[2] == 3:
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            raise ValueError("Görselin 3 kanallı (BGR) olduğundan emin olun.")

        # Görseli yeniden boyutlandır ve normalize et
        resized = cv2.resize(rgb_img, image_size)
        img_array = resized.astype(np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, H, W, 3)

        # Model ile tahmin yap
        prediction = model.predict(img_array)[0][0]
        label = "Köpek" if prediction > 0.5 else "Kedi"
        confidence = prediction if prediction > 0.5 else 1 - prediction
        text = f"Tahmin: {label} ({confidence:.2f})"

        # Üzerine yazı yaz
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        color = (0, 255, 0) if label == "Köpek" else (255, 0, 0)
        thickness = 2
        position = (10, 30)

        cv2.putText(annotated_img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

        return annotated_img



    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.predict_and_annotate(img.value,self.model)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_CatOrDog(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()