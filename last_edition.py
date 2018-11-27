import numpy as np
import cv2
import math
from sklearn.externals import joblib
import contral

def loadproject():
    initPicture = getOnePicture()
    Area1, Area2, Area3, Area4 = RectDetect(initPicture)
    num = [0, 0, 0, 0, 0, 0]
    Area = (Area1, Area2, Area3, Area4)
    j = 1
    for i in Area:
        a = array_op(i)
        num[j] = a[0]
        j += 1
    contral.move(num)

def getOnePicture():
    cap = cv2.VideoCapture(1)
    success, frame = cap.read()
    if frame is None:
        exit(1)
    cv2.namedWindow("MyWindow")
    while success and cv2.waitKey(1) == -1:
        cv2.imshow("MyWindow", frame)
        success, frame = cap.read()
    initPicture = "Screenshoot.jpg"
    cv2.imwrite(initPicture, frame)
    cv2.destroyAllWindows()
    cap.release()
    return initPicture

def ProcessImage(path):
    image = cv2.imread(path)
    gamma_img2 = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.float32)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            gamma_img2[i, j, 0] = math.pow(image[i, j, 0], 0.6)
            gamma_img2[i, j, 1] = math.pow(image[i, j, 1], 0.6)
            gamma_img2[i, j, 2] = math.pow(image[i, j, 2], 0.6)
    cv2.normalize(gamma_img2, gamma_img2, 0, 255, cv2.NORM_MINMAX)
    gamma_img2 = cv2.convertScaleAbs(gamma_img2)
    cv2.imshow("After gamma", gamma_img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return gamma_img2


def RectDetect(Imagename):
    img=cv2.pyrDown(cv2.imread(Imagename,cv2.IMREAD_UNCHANGED))
    imgs=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgs=cv2.Canny(imgs,50,100)
    ret,thresh=cv2.threshold(imgs.copy(),127,255,cv2.THRESH_BINARY)
    image,contours,hier=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    xmax,ymax,wmax,hmax=cv2.boundingRect(contours[0])
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w > wmax or h > hmax:
            xmax, ymax ,wmax ,hmax=x,y,w,h
    if wmax <= 60 or hmax <= 30:
        print("Detection failed.")
        return 0,0,0,0,0
    xmax=xmax+7
    ymax=ymax+7
    wmax=wmax-12
    hmax=hmax-12
    print(xmax,ymax,xmax+wmax,ymax+hmax)
    Area=np.asarray(img)
    Area5=Area[ymax:ymax+hmax,xmax:xmax+wmax]
    cv2.imwrite('cutted.jpg', Area5)
    Area1=Area[ymax:(ymax+round(hmax/2)),xmax:(xmax+round(wmax/2))]
    Area2=Area[ymax:(ymax+round(hmax/2)),xmax+round(wmax/2):xmax+wmax]
    Area3=Area[ymax+round(hmax/2):ymax+hmax,xmax:xmax+round(wmax/2)]
    Area4=Area[ymax+round(hmax/2):ymax+hmax,xmax+round(wmax/2):xmax+wmax]
    cv2.imwrite('cutted1.jpg', Area1)
    cv2.imwrite('cutted2.jpg', Area2)
    cv2.imwrite('cutted3.jpg', Area3)
    cv2.imwrite('cutted4.jpg', Area4)
    return Area1,Area2,Area3,Area4


def array_op(Area):
    cv2.imwrite('./gap.bmp',Area)
    Area1 = cv2.imread('./gap.bmp',0)
    ret, img2 = cv2.threshold(Area1, 127, 255, cv2.THRESH_BINARY_INV)
    img_array2 = cv2.resize(img2, (28, 28))
    imgVec = img_array2.reshape(1, 784)
    clf = joblib.load('knn.pickle')  # load model
    a = clf.predict(imgVec)
    print(a)
    return a


loadproject()