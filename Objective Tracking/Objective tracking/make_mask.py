import cv2
import numpy as np
def make_mask(imgg):
    global img
    global a,b,c,d
    a,b,c,d=[],[],[],[]
    img=imgg[:,:,::-1].copy()
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    bbox=np.zeros([len(a),4,2])
    bbox[:,0,:]=np.array(a)
    bbox[:, 1, :] = np.array(b)
    bbox[:, 2, :] = np.array(c)
    bbox[:, 3, :] = np.array(d)
    return bbox.astype(np.int)

def on_mouse(event, x, y, flags, param):
    global img, point1, point2 , a,b,c,d
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
        cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5)
        cv2.imshow('image', img2)
        a.append(point1)
        b.append(point2)
        c.append([point1[0],point2[1]])
        d.append([point2[0], point1[1]])
      #  print(a,b,c,d)



