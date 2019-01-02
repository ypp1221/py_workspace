# -*- coding:utf-8 -*-
# author:ypp
# datetime:2019/1/2 11:18
import cv2
import numpy as np
import matplotlib.pyplot as plt


def calc(image):
    #计算累计分布

    hist, bin = np.histogram(image.flatten(),256,[0,256])
    cdf = hist.cumsum()
    print cdf
    cdf_normalized = cdf * hist.max() / cdf.max()
    plt.plot(cdf_normalized,color = 'b')
    plt.hist(image.flatten(),256,[0,256],color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()
#直方图均衡化
def equalized(image):
    equ = cv2.equalizeHist(image, None)
    res = np.hstack((image,equ))
    cv2.imwrite('res.jpg',res)
    cv2.imshow('out_image', res)
#自适应直方图
def Clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    cl1 = clahe.apply(image)
    cv2.imshow('clahe image', cl1)
image = cv2.imread('../image/images.jpg',0)

#image = cv2.imread('../image/houzi.jpg',0)
cv2.namedWindow('input image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('input image', image)
equalized(image)
Clahe(image)
cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()
