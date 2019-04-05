import numpy as np
import skimage
import random
def rgb2gray(I_rgb):
    r, g, b = I_rgb[:, :, 0], I_rgb[:, :, 1], I_rgb[:, :, 2]
    I_gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return I_gray
def Ransac(px,py,nx,ny):
    leng=px.size
    innum=0
    for i in range(30):
        v=np.arange(leng)
        random.shuffle(v)
        a_cur = skimage.transform.estimate_transform('similarity', np.array([px[v[0:2]], py[v[0:2]]]).T, np.array([nx[v[0:2]], ny[v[0:2]]]).T)
        normm = a_cur(np.array([px, py]).T) - np.array([nx, ny]).T
        error = np.linalg.norm(normm, axis=1)
        ind_cur=error<1
        if np.sum(ind_cur)>innum:
            ind=ind_cur
            innum=np.sum(ind_cur)
    a=skimage.transform.estimate_transform('similarity', np.array([px[ind], py[ind]]).T, np.array([nx[ind], ny[ind]]).T)
    return a,ind