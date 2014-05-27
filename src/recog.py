# -*- coding: utf-8 -*-
import cv2
import numpy as np
import scipy

class Recog:
    masks = [
        np.array([-3, -3, 5], [-3, 0, 5], [-3, -3, 5]),
        np.array([-3, 5, 5], [-3, 0, 5], [-3, -3, -3]),
        np.array[[5, 5, 5], [-3, 0, -3], [-3, -3, -3]],
        np.array[[5, 5, -3], [5, 0, -3], [-3, -3, -3]],
        np.array[[5, -3, -3], [5, 0, -3], [5, -3, -3]],
        np.array[[-3, -3, -3], [5, 0, -3], [5, 5, -3]],
        np.array[[-3, -3, -3], [-3, 0, -3], [5, 5, 5]],
        np.array[[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]]
    ]

    def __init__(self, image):
        self.image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    def LDN(x, y):
        

    def kirschConv(x, y, i, j, k = len(masks)):
        if k == 0 : return (i, j)
        k--

        return cv2.Filter2D(self.image, dst, mask, (x, y))
        
        
