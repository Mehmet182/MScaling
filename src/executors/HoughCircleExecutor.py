"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys
import numpy as np

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

        print("self.min_radius:",self.min_radius)

    def huffeman_circle_detection(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("gray:", gray)
        gray = cv2.GaussianBlur(gray, (9, 9), 2, 2)
        print("gray2:", gray.shape)
        gray = gray.astype(np.uint8)

        circles = cv2.HoughCircles(
            gray, cv2.HOUGH_GRADIENT, dp=1, minDist=10,
            param1=100, param2=50,
            minRadius=20, maxRadius=100
        )

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for c in circles:
                print(c)
                cx, cy, r = c
                cv2.circle(img, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
                cv2.circle(img, (cx, cy), r, (0, 0, 255), 2, 8, 0)
        else:
            print("Daire bulunamadı.")

        return img

    def combine_images_side_by_side(self, img1, img2, target_size=(512, 512)):
        """
        İki resmi sabit bir boyuta getirerek (default: 512x512), yan yana birleştirir.
        Gri görüntüler otomatik olarak BGR formatına çevrilir.
        """

        # Gri görüntüyse BGR'a çevir
        if len(img1.shape) == 2:
            img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
        if len(img2.shape) == 2:
            img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

        # Sabit boyuta yeniden boyutlandır
        img1_resized = cv2.resize(img1, target_size)
        img2_resized = cv2.resize(img2, target_size)

        # Yan yana birleştir
        combined = cv2.hconcat([img1_resized, img2_resized])
        return combined

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img2 = Image.get_frame(img=self.image2, redis_db=self.redis_db)


        img_circle = self.huffeman_circle_detection(img.value)

        img.value = self.combine_images_side_by_side(img.value, img_circle)

        img2.value = self.combine_images_side_by_side(img.value, img2.value)

        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)

        self.image2 = Image.set_frame(img=img2, package_uID=self.uID, redis_db=self.redis_db)

        #print("img type:", type(img), "img.value type:", type(img.value))
        #print("img2 type:", type(img2), "img2.value type:", type(img2.value))

        packageModel = build_response_Circle(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()