import pyqrcode
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import cv2
repeats=5
#Encrpytion generating "key1"
code=pyqrcode.create("thisiskey")
code2=pyqrcode.create("thisiskey2")
#read key1 and show it
code.png('code.png',quiet_zone=0, scale=10, module_color=[1, 1, 1, 128], background=[255,255,255,155])
imgkey=cv2.imread("code.png")

code2.png('code2.png',quiet_zone=0, scale=10, module_color=[1,1,1, 128], background=[255,255,255,155])
imgkey2=cv2.imread("code2.png")

#imgkey=cv2.medianBlur(imgkey,45)
print(np.shape(imgkey))
##imgkey22=[[[]]]
##imgkey22=np.array(imgkey22)
dimen=np.shape(imgkey)
imgkey[:,:,0]=cv2.resize (np.tile(imgkey[:,:,0],repeats),(dimen[0],dimen[1]))
imgkey[:,:,1]=cv2.resize (np.tile(imgkey[:,:,1],repeats),(dimen[0],dimen[1]))
imgkey[:,:,2]=cv2.resize  (np.tile(imgkey[:,:,2],repeats),(dimen[0],dimen[1]))
cv2.imshow('img',(imgkey))

dimen=np.shape(imgkey2)
imgkey2[:,:,0]=cv2.resize (np.tile(imgkey2[:,:,0],repeats),(dimen[0],dimen[1]))
imgkey2[:,:,1]=cv2.resize (np.tile(imgkey2[:,:,1],repeats),(dimen[0],dimen[1]))
imgkey2[:,:,2]=cv2.resize  (np.tile(imgkey2[:,:,2],repeats),(dimen[0],dimen[1]))
cv2.imshow('img2',(imgkey2))

imgrevisit=imgkey+imgkey2
cv2.imshow('imgrevisit',(imgrevisit))

imgrevisit-=imgkey
cv2.imshow('imgrevisit2',(imgrevisit))

