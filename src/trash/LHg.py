# -*- coding: utf-8 -*-
import cv2
import numpy as np
import scipy.signal as signal


image = cv2.imread("mirror.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
sigma = 0.3

# valores para rotações de x e y
k = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1) ]


# filtro gaussian
def G(x, y, sigma):
    a = 1/(2 * np.pi * (sigma**2))
    b = -(((x**2)+(y**2))/(2*(sigma**2)))
    c = a * np.exp(b)
    return c

#funcao para obter os resultado dos dois filtros
# sendo "a" a que foi alvo da rotação
def M(x, y, sigma, k):
    a = G(x + k[0], y + k[1], sigma)
    b = G(x, y, sigma)
    return a, b

# criar os arrays com dimensao para acolherem os 
# resultados computados para cada pixel
code1 = np.array([[0 for x in image] for x in image[0]])
code2 = np.array([[0 for x in image] for x in image[0]])
masks = []

# criar as 8 mascaras
# as mascaras aqui sao criadas com a mesma dimensao da imagem
for i in range(0,7):
    print "criar mascara %d" % i
    for y in range(len(image)):
        for x in range(len(image[y])):
            code1[y][x], code2[y][x] = M(x, y, sigma, k[i])
    masks.append(signal.convolve2d(code1, code2))

# o resultado da convulsao da imagem com as mascaras
# dá origem a manchas pretas sem áreas brancas visíveis (a olho nu)
# no entanto alguns valores (muito poucos) são detectáveis
#for i in range(0,7):
mask = masks[4]
im = signal.convolve2d(image, mask);
imagem = im - 255 * -1
cv2.imwrite("im.jpg", imagem)
#cv2.imshow("im", imagem)
#cv2.waitKey(1500)



