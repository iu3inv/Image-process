import numpy as np
import skimage
from help import Ransac
import cv2
def applyGeometricTransformation(startXs, startYs, newXs, newYs, bbox):
    F=startXs.shape[1]
    newbbox=np.zeros(bbox.shape)
    Xs=-np.ones(startXs.shape)
    Ys=-np.ones(startXs.shape)
    for i in range(F):
        pos=newXs[:,i]!=-1
        px=startXs[:,i][pos]
        nx=newXs[:,i][pos]
        py=startYs[:,i][pos]
        ny = newYs[:, i][pos]

        # aa = skimage.transform.estimate_transform('similarity', np.array([px,py]).T,np.array([nx,ny]).T)
        # normm=aa(np.array([px, py]).T) - np.array([nx, ny]).T
        # error=np.linalg.norm(normm,axis=1)
        # print(error)
        #
        #
        # ind=error<200
        # a = skimage.transform.estimate_transform('similarity', np.array([px[ind], py[ind]]).T,np.array([nx[ind], ny[ind]]).T)

        # ind=np.argsort(error)
        # bound=round(error.size/2)
        # a = skimage.transform.estimate_transform('similarity', np.array([px[ind[:bound]], py[ind[:bound]]]).T, np.array([nx[ind[:bound]], ny[ind[:bound]]]).T)

        a,ind=Ransac(px,py,nx,ny)

        curbox=a(bbox[i,:,:])
        newbbox[i,:,:]=curbox
        #print(curbox)
        [downx, downy, w, h] = cv2.boundingRect(curbox.astype(int))
        upx=downx+w
        upy=downy+h
        # upx=np.round((curbox[1][0]+curbox[3][0])/2)
        # downx=np.round((curbox[0][0]+curbox[2][0])/2)
        # upy=np.round((curbox[1][1]+curbox[2][1])/2)
        # downy=np.round((curbox[0][1]+curbox[3][1])/2)
        # newbbox[i, :, :]=np.array([[downx,downy],[upx,upy],[downx,upy],[upx,downy]])

      #  newbbox[i,:,:]=np.round(a(bbox[i,:,:]))
      #  newbbox[i,0,:]=a(bbox[i,:,:])[0,:]
      #  newbbox[i, 1, :]=a(bbox[i,:,:])


        # Xs[:nx[ind[:bound]].size,i]=nx[ind[:bound]]
        # Ys[:ny[ind[:bound]].size,i]=ny[ind[:bound]]
        nnx=nx[ind]
        nny=ny[ind]
        ind_fin=(nnx < upx) & (nnx > downx)&(nny<upy)&(nny>downy)
        Xs[:nnx[ind_fin].size, i] = nnx[ind_fin]
        Ys[:nny[ind_fin].size, i] = nny[ind_fin]


        # print(bound)
        # print(newbbox.astype(np.int))
    return Xs,Ys,newbbox
