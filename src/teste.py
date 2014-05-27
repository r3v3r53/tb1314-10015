import cv2
import numpy as np

img = cv2.imread('mirror.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

kernel = np.array([ [-3,-3,5],
                    [-3,0,5],
                    [-3,-3,5] ],np.float32) # kernel should be floating point type.

kernel1 = np.array([ [-3,5,5],
                    [-3,0,5],
                     [-3,-3,-3] ],np.float32) 
kernel2 = np.array([ [5,5,5],
                     [-3,0,-3],
                     [-3,-3,-3] ],np.float32) 
kernel3 = np.array([ [5,5,-3],
                     [5,0,-3],
                     [-3,-3,-3] ],np.float32) 
kernel4 = np.array([ [5,-3,-3],
                     [5,0,-3],
                     [5,5,-3] ],np.float32) 

new_img1 = cv2.filter2D(img,-1,kernel) # ddepth = -1, means destination image has depth same as input image.
new_img2 = cv2.filter2D(img,-1,cv2.flip(kernel1,-1))
new_img3 = cv2.filter2D(img,-1,kernel2)
new_img4 = cv2.filter2D(img,-1,kernel3)
new_img5 = cv2.filter2D(img,-1,kernel4)
print np.amax(new_img1), np.amax(new_img2), np.amax(new_img3), np.amax(new_img4), np.amax(new_img5)
print np.amin(new_img1), np.amin(new_img2), np.amin(new_img3), np.amin(new_img4), np.amin(new_img5)
cv2.imshow('img',img)
cv2.imshow('new',new_img1)
cv2.imshow('new1',new_img2)
cv2.imshow('new2',new_img3)
cv2.imshow('new3',new_img4)
cv2.imshow('new4',new_img5)

cv2.waitKey(0)
cv2.destroyAllWindows()
