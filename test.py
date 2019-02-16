import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import cv2
img=cv2.imread("ronaldo.jpg")
##cv2.imshow('img',img)
dimen=(np.shape(img))
sign=np.reshape(img,(np.size(img)))
##plt.plot(sign)
##plt.show()
#sign=(img[:][:][:])
##plt.plot(sign)
key=np.int32(10*np.sin(np.linspace(1,10,100)))
newsig=sig.convolve(key,sign)
##plt.figure()
##plt.plot(newsig)
print("Start")
recoveredsig,remain=sig.deconvolve(newsig,key)
print("End")
##plt.figure()
##plt.figure()
#plt.plot(recoveredsig)
#plt.show()

cv2.imshow('img2',np.reshape(np.uint8(recoveredsig),dimen))












#plt.show()
#for i in range

##x=np.linspace(0,100,200)
##y=y=np.cos(-x/6.0)
##x2=np.linspace(0,100,150)
##y2=y=np.cos(-x2/6.0)
###f=sig.resample(y,100)
##a=sig.convolve(y,y)
##xnew = np.linspace(0, 10, 100)
##plt.plot(a)
##plt.show()
