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
#from components.MScaling.src.utils.utils import load_models


class CatOrDog(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        print(self.request.data)
        self.request.model = PackageModel(**(self.request.data))

        self.image = self.request.get_param("inputImage")

        #self.model = bootstrap["model"]

    """
    @staticmethod
    def bootstrap(config: dict) -> dict:
        model = load_models(config=config)
        return {"model": model}
"""

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}


    #def predict_traffic_sign(img):
     #   return img

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        #img.value = self.predict_traffic_sign(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_CatOrDog(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()