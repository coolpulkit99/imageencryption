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
cv2.imshow('Key',(imgkey))
cv2.waitKey(0)
cv2.destroyAllWindows()
#Press 0 after image is displayed to continue with the execution

height, width, channels = imgkey.shape

for x in range(0, width):
    for y in range(0, height):
        color = imgkey[x,y]
        if (color[0] != 255 or color[1] != 255 or color[2] != 255):
            value = x
quietZone = width - value

imgkey = imgkey[quietZone:height-quietZone, quietZone:width-quietZone]

cv2.imshow('Cropped key',(imgkey))
cv2.waitKey(0)
cv2.destroyAllWindows()

img=cv2.imread("ronaldo.jpg")
cv2.imshow('img1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

dimen=(np.shape(img))
print(dimen)
imgkey2=cv2.resize(imgkey,(dimen[1],dimen[0]))
cv2.imshow('img2',(imgkey2))
cv2.waitKey(0)
cv2.destroyAllWindows()

imgkeystraight=np.reshape(imgkey2,(np.size(img)))


sign=np.reshape(img,(np.size(img)))
encrypimg=np.int32(sign)*imgkeystraight
key=np.int32(10*np.sin(np.linspace(1,10,10)))
newsig=sig.convolve(key,encrypimg)
print("Start")
recoveredsig,remain=sig.deconvolve(newsig,key)
print("End")

cv2.imshow('img3',np.reshape(np.uint8(np.divide(recoveredsig,imgkeystraight)),dimen))
cv2.waitKey(0)
cv2.destroyAllWindows()
