# -*- coding: utf-8 -*-
import cv2
import numpy as np
import scipy.signal as signal

class Recog:
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
        # - assim ou cv2.filter2D ?
        self.convultions = [signal.convolve2d(self.image, self.masks[x]) for x in range(len(self.masks))]
        
        ldn = [[0 for x in range(len(self.image))] for x in range(len(self.image[0]))]
        for x in range(len(self.image)):
            for y in range(len(self.image[0])):
                ldn[x][y] = self.LDN(x,y)
    
        # passo seguinte: 
        # - dividir a imagem em 25 partes para calcular os histogramas ?
        # - ou o cálculo dos ldn deveriam ter sido já feitos nas subdivisoes da imagem?
        x = 0
        for i in self.convultions:
            cv2.imshow('img%d' % x, i)
            x+=1
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        


    def LDN(self, x, y):
        i = 8 * max(self.convultions[k][x][y] for k in range(len(self.masks)))
        j = min(self.convultions[k][x][y] for k in range(len(self.masks)))
        
        return i + j
        
r = Recog("mirror.jpg")
