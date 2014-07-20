# -*- coding: utf-8 -*-
import cv2
import numpy as np
import scipy.signal as signal

image = cv2.imread("mirror.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)

ldng = np.array([[0 for x in image] for x in image[0]])

for i in range(1,31,4):
    im2 = cv2.GaussianBlur(image, (i,1), 0.3)
#    cv2.imshow("lol", im2)
#    cv2.waitKey(500)

    convultion = signal.convolve2d(image, im2)
    print convultion
