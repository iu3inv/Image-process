import numpy as np
from scipy import interpolate
def estimateFeatureTranslation(startX, startY, Ix, Iy, img1, img2):
    sizec=7
    sx=int(round(startX))
    sy=int(round(startY))
    f1 = interpolate.interp2d(np.arange(sx - 20, sx + 20.01, 1), np.arange(sy-20,sy+20.01,1), img1[sy- 20: sy + 21, sx-20:sx+21], kind='linear')
    f2 = interpolate.interp2d(np.arange(sx - 20, sx + 20.01, 1), np.arange(sy-20,sy+20.01,1), img2[sy - 20: sy + 21, sx-20:sx+21], kind='linear')
    fx = interpolate.interp2d(np.arange(sx - 20, sx + 20.01, 1), np.arange(sy-20,sy+20.01,1), Ix[sy- 20: sy + 21, sx-20:sx+21], kind='linear')
    fy = interpolate.interp2d(np.arange(sx - 20, sx + 20.01, 1), np.arange(sy-20,sy+20.01,1), Iy[sy- 20: sy + 21, sx-20:sx+21], kind='linear')


    updateX, updateY=startX, startY
    x=np.arange(startX-sizec,startX+sizec+0.01,1)
    y = np.arange(startY - sizec, startY + sizec+0.01, 1)

    I1=f1(x,y).flatten()

    IX=fx(x,y).flatten()

    IY = fy(x, y).flatten()

    Ixx = np.dot(IX, IX)
    Iyy = np.dot(IX, IX)
    Ixy = np.dot(IX, IY)
    A = np.array([[Ixx, Ixy], [Ixy, Iyy]])
    for i in range(80):
        if updateX<sizec or updateX>img1.shape[1]-sizec or updateY<sizec or updateY>img1.shape[0]-sizec:
            updateX, updateY=-1,-1
            break
        x_update=np.arange(updateX-sizec,updateX+sizec+0.01,1)
        y_update = np.arange(updateY - sizec, updateY + sizec+0.01, 1)
        I2=f2(x_update,y_update).flatten()

        It=I1-I2

        b=np.array([[np.dot(It,IX)],[np.dot(It,IY)]])


        xchange , ychange =0.1* np.linalg.solve(A, b)


        updateX=updateX+xchange
        updateY=updateY+ychange
      #  print(updateX , updateY)
    newX, newY=updateX,updateY
    return newX, newY