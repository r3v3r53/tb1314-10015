#-*-coding: utf-8-*-
import cv2
import numpy as np
import scipy.signal as signal

class Kirsh():
    '''
    Classe para criacao de codigo LH para uma determinada imagem
    utilizando mascaras de Kirsh
    '''

    def __init__(self, img):
        '''
        Constructor
        - Recebe a localizacao de uma imagem
        - cria as mascaras kirsh
        - efectua a convulsao da imagem com as mascaras
        - calcula os codigos LDN para cada pixel da imagem
          com o auxilio do metodo LDN
        - da inicio a construcao do histograma

        @arg img: localizacao e nome da imagem a analizar
        '''
        self.image = cv2.imread(img, cv2.CV_LOAD_IMAGE_GRAYSCALE)
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
                self.ldn[x][y] = self.__LDN(x,y)
        self.__histogram()

    def __histogram(self):
        '''
        Metodo para construcao do histograma da imagem
        calcula o histograma para cada parte da imagem
        de acordo com o numero de divisoes pretendido
        os resultados sao concatenados na variavel local "lh"
        '''
        len_x = len(self.ldn)
        len_y = len(self.ldn[0])
        div = self.divisions
        for i in range(div):
            for j in range(div):
                cur = self.image[i*len_x/div:i*len_x/div + len_x/div,
                                 j*len_y/div: j*len_y/div + len_y/div]
                hist, bin_edges = np.histogram(cur,
                                               div,
                                               density=True,
                                               weights=cur)
                ret = np.frombuffer(hist * np.diff(bin_edges))
                self.lh = np.concatenate((self.lh, ret))

    def __LDN(self, x, y):
        '''
        Metodo para calcular o codigo LDN para um pixel da imagem
        
        @arg x: cordenada do pixel a analizar 
        @arg y: cordenada do pixel a analizar
        @return: codigo LDN 
        '''
        n_masks = len(self.masks)
        i = 8 * max(self.convultions[k][x][y]
                    for k in range(n_masks))
        j = min(self.convultions[k][x][y]
                for k in range(n_masks))
        return i + j

    def code(self):
        '''
        Metodo para devolver o codigo lh
        calculado para a imagem
        
        @return: codigo LH calculado 
        '''
        return self.lh
