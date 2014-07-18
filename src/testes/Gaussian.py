import cv2
import numpy as np
import scipy.signal as signal

class Gaussian():
    def __init__(self, image, sigma):
        self.sigma = sigma
        self.image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        self.k = [(0,1), (1,1), (1,0), (1,-1),
                  (0,-1), (-1,-1), (-1,0), (-1,1) ]
        self.code1 = np.array([[0 for x in self.image] for x in self.image[0]])
        self.code2 = np.array([[0 for x in self.image] for x in self.image[0]])
        self.masks = []
        self.buildMasks()
        self.divisions = 5
        self.convultions = [
            signal.convolve2d(self.image, mask) for mask in self.masks
        ]
        self.lh = []
        self.ldn = np.array(
            [[0 for x in range(len(self.image))]
             for x in range(len(self.image[0]))]
        )
        for x in range(len(self.image)):
            for y in range(len(self.image[0])):
                self.ldn[x][y] = self.LDN(x,y)
        self.histogram()

    # filtro gaussian
    def G(self, x, y, sigma):
        a = 1/(2 * np.pi * (sigma**2))
        b = -(((x**2)+(y**2))/(2*(sigma**2)))
        c = a * np.exp(b)
        return c

    #funcao para obter os resultado dos dois filtros
    # sendo "a" a que foi alvo da rotacao

    def M(self, x, y, sigma, k):
        a = self.G(x + k[0], y + k[1], sigma)
        b = self.G(x, y, sigma)
        return a, b

    # criar as 8 mascaras
    # as mascaras aqui sao criadas com a mesma
    # dimensao da imagem
    def buildMasks(self):
        for i in range(0,7):
            for y in range(len(self.image)):
                for x in range(len(self.image[y])):
                    self.code1[y][x], self.code2[y][x] = \
                    self.M(x, y, self.sigma, self.k[i])
        self.masks.append(signal.convolve2d(self.code1, self.code2))

        

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
                self.lh = np.concatenate((self.lh, ret))

    def LDN(self, x, y):
        n_masks = len(self.masks)
        i = 8 * max(self.convultions[k][x][y]
                    for k in range(n_masks))
        j = min(self.convultions[k][x][y]
                for k in range(n_masks))
        return i + j

    def convolve(self, masks):
        self.convultions = [signal.convolve2D(self.image, mask)
                            for mask in masks]

    def code(self):
        return self.lh
