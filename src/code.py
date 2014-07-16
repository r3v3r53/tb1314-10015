import cv2
import numpy as np
import scipy.signal as signal

class LH():
    def __init__(self, image, masks):
        self.image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        self.divisions = 5
        self.masks = masks
        self.convultions = [
            signal.convolve2d(self.image, mask for mask in self.masks)
        ]
        self.ldn = np.array(
            [[0 for x in self.image] for x in self[image[0]]]
        )
        for x in range(len(self.image)):
            for y in range(len(self.image[0])):
                self.ldn[x][y] = self.LDN(x,y)
        self.histogram()
                        

    def histogram(self):
        len_x = len(self.ldn)
        len_y = len(self.ldn[0])
        for i in range(self.divisions):
            for j in range(self.divisions):
                cur = self.image[i*len_x/5:i*len_x/5 + len_x/5, 
                                j*len_y/5: j*len_y/5 + len_y/5]
                hist, bin_edges = np.histogram(cur, 
                                               5, 
                                               density=True, 
                                               weights=cur)
                ret = np.frombuffer(hist * np.diff(bin_edges))
                self.ldn = np.concatenate((self.ldn, ret))
                
    def LDN(self, x, y):
        i = 8 * max(self.convultions[k][x][y] \
                    for k in range(n_masks))
        j = min(self.k_convultions[k][x][y] \
                for k in range(n_masks))
        return i + j

    def convolve(self, masks):
        self.convultions = [signal.convolve2D(self.image, mask) \
                           for mask in masks]

    def code(self):
        return self.ldn

class Kirsh(LH):

    def __init__(self, image):
        self.masks = [
            np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),
            np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]),
            np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
            np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]]),
            np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),
            np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),
            np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),
            np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
        ]
        super().__init__(image, self.masks)

class Gaussian(LH):
    def __init__(self, image, sigma):
         self.masks = [
             cv2.GaussianBlur(self.image, (x, 1), sig) 
             for x in range(1,31,4)
         ]
         super().__init__(image, self.masks)
