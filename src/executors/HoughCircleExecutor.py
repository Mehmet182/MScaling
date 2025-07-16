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
from components.MScaling.src.utils.response import build_response_Circle
from components.MScaling.src.models.PackageModel import PackageModel


class HoughCircleExecutor(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))



        #self.min_radius = self.request.get_param("MinRadius")
        #print(self.min_radius)

        #self.max_radius = self.request.get_param("MaxRadius")
        #print(self.max_radius)

        self.image = self.request.get_param("inputImage")


    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}


    def HoughCircle(self,img):
       return cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=10,param1=100, param2=50, minRadius=self.min_radius, maxRadius=self.max_radius)

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.HoughCircle(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_Circle(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()