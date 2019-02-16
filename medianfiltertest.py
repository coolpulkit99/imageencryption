import pyqrcode
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import cv2
code=pyqrcode.create("thisiskey")
#read key1 and show it
code.png('code.png', scale=6, module_color=[1, 1, 1, 128], background=[0xff, 0xff, 0xff])
imgkey=cv2.imread("code.png")
print(np.shape(imgkey))
cv2.imshow('img',(imgkey))
img2=cv2.medianBlur(imgkey,45)
cv2.imshow('img2',(img2))
