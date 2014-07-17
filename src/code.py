import cv2
import numpy as np
import scipy.signal as signal

# Gerar o codigo LH para uma imagem
class LH():
    def __init__(self, image, masks):
        self.image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        self.divisions = 5
        self.masks = masks
        self.convultions = [
            signal.convolve2d(self.image, mask) for mask in self.masks
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
        i = 8 * max(self.convultions[k][x][y] 
                    for k in range(n_masks))
        j = min(self.k_convultions[k][x][y] 
                for k in range(n_masks))
        return i + j

    def convolve(self, masks):
        self.convultions = [signal.convolve2D(self.image, mask) 
                            for mask in masks]

    def code(self):
        return self.ldn

#reconhecimento atraves de filtros com mascaras Kirsh
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
        LH.__init__(self, image, self.masks)

# reconhecimento atraves de filtros gaussian
class Gaussian(LH):
    def __init__(self, image, sigma):
        self.k = [(0,1), (1,1), (1,0), (1,-1), 
                  (0,-1), (-1,-1), (-1,0), (-1,1) ]
        self.code1 = np.array([[0 for x in image] for x in image[0]])
        self.code2 = np.array([[0 for x in image] for x in image[0]])
        self.masks = []
        self.buildMasks()
         
        super(Gaussian, self).__init__(image, self.masks)

    # filtro gaussian
    def G(self, x, y, sigma):
        a = 1/(2 * np.pi * (sigma**2))
        b = -(((x**2)+(y**2))/(2*(sigma**2)))
        c = a * np.exp(b)
        return c

    #funcao para obter os resultado dos dois filtros
    # sendo "a" a que foi alvo da rotacao     

    def M(self, x, y, sigma, k):
        a = G(x + k[0], y + k[1], sigma)
        b = G(x, y, sigma)
        return a, b

    # criar as 8 mascaras
    # as mascaras aqui sao criadas com a mesma 
    # dimensao da imagem
    def builMasks(self):
        for i in range(0,7):
            for y in range(len(self.image)):
                for x in range(len(self.image[y])):
                    self.code1[y][x], self.code2[y][x] = \
                    self.M(x, y, self.sigma, self.k[i])
        self.masks.append(signal.convolve2d(code1, code2))
