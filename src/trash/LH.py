# -*- coding: utf-8 -*-
import cv2
import numpy as np
import scipy.signal as signal

class LH:
    # kirsch compass masks
    k_masks = [
        np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),
        np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]),
        np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
        np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]]),
        np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),
        np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),
        np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),
        np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
    ]
    
    def __init__(self, image, shape, sig):
        self.sig = sig
        self.image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        self.g_masks = [cv2.GaussianBlur(self.image, (x, 1), sig) for x in range(1,31,4)]
        #print self.g_masks
        #print self.k_masks
        #return 0
        # criar convultions da imagem para cada uma das masks
        self.k_convultions = [signal.convolve2d(self.image, self.k_masks[x]) for x in range(len(self.k_masks))]
        self.g_convultions = [signal.convolve2d(self.image, self.g_masks[x]) for x in range(len(self.g_masks))]
        self.ldnk = np.array([[0 for x in self.image] for x in self.image[0]])
        self.ldng = np.array([[0 for x in self.image] for x in self.image[0]])
        for x in range(len(self.image)):
            for y in range(len(self.image[0])):
                self.ldnk[x][y] = self.LDNk(x,y)
                self.ldng[x][y] = self.LDNg(x,y)

        # histogramas
        lenx = len(self.ldnk)
        leny = len(self.ldnk[0])
        self.ldnk = []
        
        for i in range(5):
            for j in range(5):
                cur = self.ldnk[i*lenx/5:i*lenx/5 + lenx/5, j*leny/5: j*leny/5 + leny/5]
                hist, bin_edges = np.histogram(cur, 5, density=True, weights=cur)
                ret = np.frombuffer(hist * np.diff(bin_edges))
                self.ldnk = np.concatenate((self.ldnk, ret))
                cur = ldng[i*lenx/5:i*lenx/5 + lenx/5, j*leny/5: j*leny/5 + leny/5]
                hist, bin_edges = np.histogram(cur, 5, density=True, weights=cur)
                ret = np.frombuffer(hist * np.diff(bin_edges))
                self.ldng = np.concatenate((self.ldng, ret))
                

    def LDNk(self, x, y):
        i = 8 * max(self.k_convultions[k][x][y] for k in range(len(self.k_masks)))
        j = min(self.k_convultions[k][x][y] for k in range(len(self.k_masks)))
        return i + j

    def LDNg(self, x, y):
        i = 8 * max(self.g_convultions[k][x][y] for k in range(len(self.g_masks)))
        j = min(self.g_convultions[k][x][y] for k in range(len(self.g_masks)))
        return i + j

                                                        
    def LDNkCode(self):
        return self.ldnk

    def LDNgCode(self):
        return self.ldng
