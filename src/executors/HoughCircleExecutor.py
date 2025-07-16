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
        print(self.request.data)
        self.request.model = PackageModel(**(self.request.data))


        self.min_radius = self.request.get_param("MinRadius")
        print("self.min_radius:",self.min_radius)

        self.load_parameters()

        self.max_radius = self.request.get_param("MaxRadius")
        print("self.min_radius:",self.max_radius)

        self.image = self.request.get_param("inputImage")
        self.image2 = self.request.get_param("inputImage2")


    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def load_parameters(self):
        if self.min_radius=="MinRadius1":
            self.min_radius = 10
        elif self.min_radius=="MinRadius2":
            self.min_radius = 20
        else:
            self.min_radius = 30

        print("load_self.min_radius:",self.min_radius)

    def huffeman_circle_detection(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = cv2.GaussianBlur(gray, (9, 9), 2, 2)

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=10,
                                  param1=100, param2=50,
                                  minRadius=self.min_radius, maxRadius=self.max_radius)

        for c in circles[0, :]:
            print(c)
            cx, cy, r = c
            cv2.circle(img, (int(cx), int(cy)), 2,(0, 255, 0), 2, 8, 0)
            cv2.circle(img, (int(cx), int(cy)), int(r),(0, 0, 255), 2, 8, 0)

        return img

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.huffeman_circle_detection(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_Circle(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()