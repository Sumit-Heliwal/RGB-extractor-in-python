# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:23:12 2020

@author: Sumit
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:00:48 2020

@author: Sumit
"""

import cv2
import numpy as np
img = cv2.imread('orignall.jpg')
# shape attribute of an image matrix gives the dimensions
row,col,plane = img.shape

# here image is of class 'uint8', the range of values  
# that each colour component can have is [0 - 255]

# create a zero matrix of order same as
# original image matrix order of same dimension
temp = np.zeros((row,col,plane),np.uint8)

# store blue plane contents or data of image matrix
# to the corresponding plane(blue) of temp matrix
temp[:,:,0] = img[:,:,0]

# displaying the Blue plane image
cv2.imshow('Blue plane image',temp)
cv2.imwrite("BLUEE.png",temp)

# again take a zero matrix of image matrix shape
temp = np.zeros((row,col,plane),np.uint8)

# store green plane contents or data of image matrix
# to the corresponding plane(green) of temp matrix
temp[:,:,1] = img[:,:,1]

# displaying the Green plane image
cv2.imshow('Green plane image',temp)
cv2.imwrite("GREENN.png",temp)

# again take a zero matrix of image matrix shape
temp = np.zeros((row,col,plane),np.uint8)

# store red plane contents or data of image matrix
# to the corresponding plane(red) of temp matrix
temp[:,:,2] = img[:,:,2]

# displaying the Red plane image
cv2.imshow('Red plane image',temp)
cv2.imwrite("REDD.png",temp)