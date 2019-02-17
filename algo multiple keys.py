##import pyqrcode
##import numpy as np
##import cv2

import pyqrcode
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import cv2

#Encrpytion generating "key1"
code=pyqrcode.create("key2")
#read key1 and show it
code.png('code.png',quiet_zone=0, scale=10, module_color=[1, 1, 1, 128], background=[255,255,255,155])
imgkey=cv2.imread("code.png")
dimen=np.shape(imgkey)
imgkey[:,:,0]=cv2.resize (np.tile(imgkey[:,:,0],5),(dimen[0],dimen[1]))
imgkey[:,:,1]=cv2.resize (np.tile(imgkey[:,:,1],5),(dimen[0],dimen[1]))
imgkey[:,:,2]=cv2.resize  (np.tile(imgkey[:,:,2],5),(dimen[0],dimen[1]))
cv2.imshow('img',(imgkey))

#imgkey=cv2.medianBlur(imgkey,45)
code=pyqrcode.create("key2")
#read key1 and show it
code.png('code.png',quiet_zone=0, scale=10, module_color=[1, 1, 1, 128], background=[255,255,255,155])
imgkey2=cv2.imread("code.png")

print(np.shape(imgkey))
##imgkey22=[[[]]]
##imgkey22=np.array(imgkey22)

imgkey2[:,:,0]=cv2.resize (np.tile(imgkey[:,:,0],5),(dimen[0],dimen[1]))
imgkey2[:,:,1]=cv2.resize (np.tile(imgkey[:,:,1],5),(dimen[0],dimen[1]))
imgkey2[:,:,2]=cv2.resize  (np.tile(imgkey[:,:,2],5),(dimen[0],dimen[1]))
imgkey=imgkey+imgkey2
cv2.imshow('img',(imgkey))

#height, width, channels = imgkey.shape

##for x in range(0, width):
##    for y in range(0, height):
##        color = imgkey[x,y]
##        if (color[0] != 255 or color[1] != 255 or color[2] != 255):
##            value = x
##quietZone = width - value
##
##imgkey = imgkey[quietZone:height-quietZone, quietZone:width-quietZone]


#read image and show it
img=cv2.imread("ronaldo.jpg")
cv2.imshow('img1',img)

dimen=(np.shape(img))
print(dimen)

#realign/resize key image according to image size
imgkey2=cv2.resize(imgkey,(dimen[1],dimen[0]))
cv2.imshow('img2',(imgkey2))

#vectorize key image
imgkeystraight=np.reshape(imgkey2,(np.size(img)))

#vectorize image
sign=np.reshape(img,(np.size(img)))
#Encrypting using key1
encrypimg=np.int32(sign)*imgkeystraight
abcc=np.reshape((encrypimg),dimen)
cv2.imshow('img4',abcc)

#Encrpytion generating "key2"
key=np.int32(10*np.sin(np.linspace(1,10,10)))

#Encrypting using key2
newsig=sig.convolve(key,encrypimg)
print("Start")

#DEcrypting using key2
recoveredsig,remain=sig.deconvolve(newsig,key)
print("End")
#DEcrypting using key1
abbc=np.reshape(np.uint8(np.divide(recoveredsig,imgkeystraight)),dimen)
cv2.imshow('img3',abbc)
