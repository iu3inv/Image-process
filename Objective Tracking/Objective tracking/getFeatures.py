import numpy as np
from skimage.feature import corner_shi_tomasi, corner_peaks
from skimage.feature import corner_harris,peak_local_max
import cv2
def getFeatures(img,bbox):
    obj_num=bbox.shape[0]
    coor=[]
    maxN=0
    for i in range(obj_num):
        # row_min=min(bbox[i,:,1])
        # row_max=max(bbox[i,:,1])
        # col_min=min(bbox[i,:,0])
        # col_max = max(bbox[i, :, 0])
        [xmin,ymin,w,h]=cv2.boundingRect(bbox[i,:,:].astype(int))
        #coor.append ( corner_peaks(corner_harris(img[row_min:row_max,col_min:col_max]), min_distance=3,num_peaks=30))
        #coor.append(peak_local_max(corner_harris(img[row_min:row_max, col_min:col_max]), exclude_border=3, num_peaks=30))
        coor.append(peak_local_max(corner_harris(img[ymin:ymin+h, xmin:xmin+w]), exclude_border=2, num_peaks=30))
        maxN=max(maxN,coor[-1].shape[0])
    x=-np.ones([maxN,obj_num])
    y = - np.ones([maxN, obj_num])
    for i in range(obj_num):
        lenn=coor[i].shape[0]
        x[0:lenn,i]=coor[i][:,0]+min(bbox[i,:,1])#row
        y[0:lenn, i] = coor[i][:, 1]+min(bbox[i,:,0])#col
    return x,y




