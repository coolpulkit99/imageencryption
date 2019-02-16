import pyqrcode
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import cv2

code=pyqrcode.create("thisiskey")
code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
img=cv2.imread("code.png")
print(np.shape(img))
cv2.imshow('img',(img))
img2=cv2.resize(img,(100,150))
cv2.imshow('img2',(img2))
