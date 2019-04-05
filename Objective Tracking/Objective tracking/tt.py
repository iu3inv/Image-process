import numpy as np
from skimage.feature import corner_shi_tomasi, corner_peaks
from PIL import Image
from getFeatures import getFeatures
from make_mask import make_mask
from estimateFeatureTranslation import estimateFeatureTranslation
import cv2
from scipy import interpolate
import skimage
from applyGeometricTransformation import applyGeometricTransformation
startXs=np.array([[1],[2],[3],[4]])
startYs=np.array([[1],[2],[3],[4]])
newXs=np.array([[1],[2],[3],[4]])
newYs=np.array([[1],[2],[3],[4]])
bbox=np.array([[[1,3],[1,1],[5,3],[5,1]]])
print(applyGeometricTransformation(startXs, startYs, newXs, newYs, bbox))
cap = cv2.VideoCapture('Easy.mp4')
frames_num=cap.get(4)

a=[1,2,3,4]
ind=np.ones([1,4])
ind[1]=0
a[ind]