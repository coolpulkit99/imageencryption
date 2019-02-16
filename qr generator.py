##import pyqrcode
##import numpy as np
##import cv2

import pyqrcode
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import cv2

code=pyqrcode.create("thisiskey")
code.png('code.png', scale=6, module_color=[1, 1, 1, 128], background=[0xff, 0xff, 0xff])
imgkey=cv2.imread("code.png")
print(np.shape(imgkey))
cv2.imshow('img',(imgkey))


img=cv2.imread("ronaldo.jpg")
cv2.imshow('img1',img)
dimen=(np.shape(img))
print(dimen)
imgkey2=cv2.resize(imgkey,(dimen[1],dimen[0]))
cv2.imshow('img2',(imgkey2))

imgkeystraight=np.reshape(imgkey2,(np.size(img)))


sign=np.reshape(img,(np.size(img)))
encrypimg=np.int32(sign)*imgkeystraight
key=np.int32(10*np.sin(np.linspace(1,10,10)))
newsig=sig.convolve(key,encrypimg)
print("Start")
recoveredsig,remain=sig.deconvolve(newsig,key)
print("End")

cv2.imshow('img3',np.reshape(np.uint8(np.divide(recoveredsig,imgkeystraight)),dimen))
