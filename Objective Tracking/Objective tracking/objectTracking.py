import cv2
from make_mask import make_mask
from getFeatures import getFeatures
from help import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import signal
from PIL import Image
import shutil
import glob
from estimateAllTranslation import  estimateAllTranslation
from applyGeometricTransformation import applyGeometricTransformation
def objectTracking(name,track,maxframenum):
    capture = cv2.VideoCapture(name)
    flag=capture.isOpened()
    fps = 30
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    VidX=int(capture.get(3))
    VidY=int(capture.get(4))
    videoWriter = cv2.VideoWriter('res_medium_track1.avi', fourcc, fps, (VidX,VidY))
    num=1
    x_save=[]
    y_save=[]
    while(flag):
        flag, frame = capture.read()
        if flag and num<maxframenum:
            if num==1:
                bbox = make_mask(frame)
                frame_gray_old=rgb2gray(frame)

                y_pre,x_pre=getFeatures(frame_gray_old, bbox)
                for i in range(bbox.shape[0]):
                    [xmin, ymin, w, h] = cv2.boundingRect(bbox[i, :, :])
                    cv2.rectangle(frame, (xmin,ymin),(xmin+w,ymin+h), (255, 0, 0), 1)
                  #  cv2.rectangle(frame, tuple(bbox[i,0,:]),tuple(bbox[i,1,:]) ,(255, 0, 0), 1)
                for i in range(x_pre.size):
                    if x_pre.flatten()[i]!=-1:
                        cv2.circle(frame, (x_pre.flatten()[i].astype(int), y_pre.flatten()[i].astype(int)), 1, (255, 0, 0))

             #   cv2.imshow('cur', frame)
                videoWriter.write(frame)
               # cv2.waitKey(0)
            else:
                frame_gray_new=rgb2gray(frame)
                frame2=frame.copy()
                frame3=frame.copy()
               # cv2.imshow('s',frame_gray_new.astype(np.uint8))
               # cv2.waitKey(0)
                Xs,Ys=estimateAllTranslation(x_pre, y_pre, frame_gray_old, frame_gray_new)
                Xss,Yss,bbox=applyGeometricTransformation(x_pre, y_pre, Xs, Ys, bbox)
                indbox=np.ones(bbox.shape[0])
                for i in range(bbox.shape[0]):

                    #print(bbox[i,0,:])
                    [xmin, ymin, w, h] = cv2.boundingRect(bbox[i, :, :].astype(int))

                    if (xmin<20 or xmin+w>VidX-20 or ymin<20 or ymin+h>VidY-20):
                        indbox[i] = 0

                    cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), (255, 0, 0), 1)
                    cv2.rectangle(frame2, (xmin, ymin), (xmin + w, ymin + h), (255, 0, 0), 1)
                    cv2.rectangle(frame3, (xmin, ymin), (xmin + w, ymin + h), (255, 0, 0), 1)

                    # cv2.rectangle(frame, tuple(bbox[i,0,:]),tuple(bbox[i,1,:]) ,(255, 0, 0), 1)
                    # cv2.rectangle(frame2, tuple(bbox[i, 0, :]), tuple(bbox[i, 1, :]), (255, 0, 0), 1)
                    # cv2.rectangle(frame3, tuple(bbox[i, 0, :]), tuple(bbox[i, 1, :]), (255, 0, 0), 1)
                print(indbox)
                if track:
                    x_save=np.hstack((x_save,Xss.flatten()))
                    y_save=np.hstack((y_save,Yss.flatten()))



                bbox=bbox[indbox==1,:,:]
                for i in range(Xs.size):
                    if Xs.flatten()[i]!=-1:
                        #print(Xss.flatten()[i].astype(int))
                        cv2.circle(frame, (x_pre.flatten()[i].astype(int), y_pre.flatten()[i].astype(int)), 1, (255, 0, 0))
                        cv2.circle(frame2, (Xs.flatten()[i].astype(int), Ys.flatten()[i].astype(int)), 1, (0, 0, 255))
                        if not track:
                            cv2.circle(frame3, (Xss.flatten()[i].astype(int),Yss.flatten()[i].astype(int)), 1, (0, 255, 0))
                if track:
                    for i in range(x_save.size):
                        cv2.circle(frame3, (x_save[i].astype(int), y_save[i].astype(int)), 1, (0, 255, 0))
             #   cv2.imshow('cur',frame)
              #  cv2.imshow('cur2', frame2)
                cv2.imshow('cur3', frame3)
                videoWriter.write(frame3)
                frame_gray_old=frame_gray_new.copy()
                y_pre, x_pre = getFeatures(frame_gray_old, bbox)
               #  print(Yss)
               #  print(getFeatures(frame_gray_old, bbox)[0])
                #y_pre, x_pre =Yss,Xss
                cv2.waitKey(80)

        else:
            break
        num=num+1
        print(num)

    capture.release()
    videoWriter.release()
if __name__=="__main__":
    objectTracking('Medium.mp4',1,360)





