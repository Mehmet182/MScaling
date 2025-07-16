"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.MScaling.src.utils.response import build_response_Blur
from components.MScaling.src.models.PackageModel import PackageModel


class GaussianBlurExecutor(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        print(self.request.data)
        self.request.model = PackageModel(**(self.request.data))

        self.ksize = self.request.get_param("KSize")
        print(self.ksize)

        self.sigmax = self.request.get_param("SigmaX")
        print(self.sigmax)

        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}


    def GaussianBlur(self,img):

        return cv2.GaussianBlur(img,(3,3) ,5)

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.GaussianBlur(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_Blur(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()