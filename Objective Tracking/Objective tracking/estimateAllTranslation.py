import numpy as np
from estimateFeatureTranslation import estimateFeatureTranslation
def estimateAllTranslation(startXs,startYs,img1,img2):
    N,F=startXs.shape
    print(startXs.shape)
    newXs=np.zeros([N,F])
    newYs = np.zeros([N, F])
    Iy, Ix = np.gradient(img1)
    for i in range(N):
        for j in range(F):
            if startXs[i][j]==-1:
                newXs[i][j]=-1
                newYs[i][j] = -1
            else:
                startX=startXs[i][j]
                startY=startYs[i][j]
                newX, newY=estimateFeatureTranslation(startX, startY, Ix, Iy, img1, img2)
                newXs[i][j]=newX
                newYs[i][j] =newY
    return newXs, newYs