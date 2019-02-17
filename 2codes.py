import pyqrcode
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import cv2
code=pyqrcode.create("thisiskey1")
#read key1 and show it
code.png('code.png', scale=16, module_color=[1, 1, 1, 128], background=[155, 155, 155,255])
imgkey=cv2.imread("code.png")
print(np.shape(imgkey))
cv2.imshow('img',(imgkey))
img2=cv2.medianBlur(imgkey,45)
cv2.imshow('img2',(img2))
code=pyqrcode.create("thisiskey2")
code.png('code2.png', scale=16, module_color=[155, 155, 155, 128], background=[1, 1, 1,255])
imgkey2=cv2.imread("code2.png")
print(np.shape(imgkey))
cv2.imshow('img5',(imgkey2))
img55=cv2.medianBlur(imgkey,45)
cv2.imshow('img3',(img2))
img3=imgkey+imgkey2
img4=img55+img2

cv2.imshow('img4',(img3))
cv2.imshow('img5',(img4))
