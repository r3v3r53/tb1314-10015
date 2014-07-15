# -*- coding: utf-8 -*-
import cv2
import numpy as np
import scipy.signal as signal

class LH:
    # kirsch compass masks
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
        # criar convultions da imagem para cada uma das masks
        self.convultions = [signal.convolve2d(self.image, self.masks[x]) for x in range(len(self.masks))]
        ldnk = np.array([[0 for x in self.image] for x in self.image[0]])
        ldng = np.array([[0 for x in self.image] for x in self.image[0]])
        for x in range(len(self.image)):
            for y in range(len(self.image[0])):
                ldnk[x][y] = self.LDNk(x,y)
                ldng[x][y] = self.LDNg(x,y)

        # histogramas
        lenx = len(ldnk)
        leny = len(ldnk[0])
        self.ldnk = []
        for i in range(5):
            for j in range(5):
                cur = ldnk[i*lenx/5:i*lenx/5 + lenx/5, j*leny/5: j*leny/5 + leny/5]
                hist, bin_edges = np.histogram(cur, 5, density=True, weights=cur)
                ret = np.frombuffer(hist * np.diff(bin_edges))
                self.ldnk = np.concatenate((self.ldnk, ret))

    def LDNk(self, x, y):
        i = 8 * max(self.convultions[k][x][y] for k in range(len(self.masks)))
        j = min(self.convultions[k][x][y] for k in range(len(self.masks)))
        return i + j
    
    def LDNg(self, x, y):
        
    def G(self, x, y, sig):
        return (1 / (2 * math.pi * sig ** 2)) * math.exp( -((x ** 2 + y ** 2) / (2 * sig ** 2)))

    def MasksG(self, x, y, sig):
        

                                                        
    def code(self):
        return self.ldnk
