import numpy as np
from skimage.feature import corner_shi_tomasi, corner_peaks
from PIL import Image
from getFeatures import getFeatures
from make_mask import make_mask
from estimateFeatureTranslation import estimateFeatureTranslation
import cv2
from scipy import interpolate
import skimage
def rgb2gray(I_rgb):
    r, g, b = I_rgb[:, :, 0], I_rgb[:, :, 1], I_rgb[:, :, 2]
    I_gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return I_gray
img_rgb=np.array(Image.open('1.jpg'))
img=rgb2gray(img_rgb)
bbox=np.array([[[20,20],[200,20],[200,200],[20,200]],[[300,300],[300,400],[400,300],[400,400]]])

cv2.circle(img, (1,100), 100, (0, 0, 255))
cv2.imshow('1',img/256)
cv2.waitKey(0)
# bbox=make_mask(img_rgb)
# print(bbox)
# print(getFeatures(img,bbox)[1])
h=np.zeros([150,150])
hh=np.zeros([150,150])
o=np.ones([5,5])
h[113:118,114:119]=o
hh[115:120,117:122]=o
Iy,Ix=np.gradient(h)
startX=3
startY=3
img1=np.zeros([6,6])
img2=np.zeros([6,6])
img1[3][3]=1
img2[3][3]=1
print(img2[np.arange(startY - 1, startY + 1.01, 1).astype(np.int), np.arange(startX - 1, startX + 1.01, 1).astype(np.int)])
#f = interpolate.interp2d(np.arange(startX - 1, startX + 1.01, 1), np.arange(startY - 1, startY + 1.01, 1), img2[np.arange(startY - 1, startY + 1.01, 1).astype(np.int), np.arange(startX - 1, startX + 1.01, 1).astype(np.int)],kind='linear')
print(estimateFeatureTranslation(119, 118, Ix, Iy, h, hh))

# a=skimage.transform.estimate_transform('similarity',np.array([[1,3],[2,5],[3,5]]),np.array([[1,3],[2,5],[3,5]]))
# print(a(np.array([[1,3],[2,5],[3,5]])))