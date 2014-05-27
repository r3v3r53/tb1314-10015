# -*- coding: utf-8 -*-
import cv2
import numpy as np
import scipy

class Recog:
    masks = [
        np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),
        np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]),
        np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
        np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]]),
        np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),
        np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),
        np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),
        np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
    ]
    

    def __init__(self, image):
        
        self.image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ldn = [[0 for x in range(len(self.image))] for x in range(len(self.image[0]))]
        for x in range(len(image)):
            for y in range(len(image[0])):
                ldn[x][y] = self.LDN(x,y)
        print np.amax(ldn), np.amin(ldn)

    def LDN(self, x, y):
        i, j = self.kirschConv(x, y)
        return 8 * i + j

    def kirschConv(self, x, y, i = None, j = None, k = len(masks)):
        if k == 0 : return (i, j)
        k-=1
        conv = cv2.filter2D(self.image, -1, self.masks[k], (x, y))
        if i == None: i = np.amax(conv)
        if j == None: j = np.amin(conv)
        return self.kirschConv(x, y, max(i, np.amax(conv)), min(i, np.amin(conv)), k)
        
r = Recog("mirror.jpg")
