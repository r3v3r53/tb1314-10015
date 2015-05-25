#-*-coding: utf-8-*-
import cv2
import numpy as np
import scipy.signal as signal

class LDNg():
    '''
    Classe para criacao de codigo LH para uma determinada imagem
    utilizando mascaras Gaussian
    '''

    def __init__(self, img, sigma):
        '''
        Constructor
        - Recebe a localizacao de uma imagem
        
        @arg img: localizacao e nome da imagem a analizar
        @arg sigma largura da curvatura de bell (precisao)
        '''

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
                cur = self.ldn[i*len_x/div:i*len_x/div + len_x/div,
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
