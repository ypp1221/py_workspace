# -*- coding: utf-8 -*-
import cv2
import  matplotlib.pyplot as plt
import  numpy as np

import sys
print(sys.executable)
def image_hist(image):
    color = ('blue','green','red')
    for i, color in enumerate(color):
        hist = cv2.calcHist(images=[image],channels=[i],mask=None,histSize=[256],ranges=[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()


def bar_show(image):
    plt.hist(image.ravel,256,[0,256])
    plt.show()


def use_mask(image):
    mask = np.zeros(image.shape,np.uint8)
    print(image.shape)
    print(mask.shape)
    #构造遮罩层
    mask[20:160,20:160] = 255
    #进行and运算
    masked_image = cv2.bitwise_and(image,image,mask=mask)

    #统计灰度
    hist_full = cv2.calcHist([image], [0],None,[256],[0,256])
    hist_mask = cv2.calcHist([image], [0],mask,[256],[0,256])
    #画图
    plt.subplot(221),plt.imshow(image,'gray')
    plt.subplot(222),plt.imshow(mask,'gray')
    plt.subplot(223),plt.imshow(masked_image,'gray')
    plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
    plt.show()
im = cv2.imread('../image/build.jpg',0)
cv2.namedWindow("input image",cv2.WINDOW_AUTOSIZE)
cv2.imshow('input image', im)
#use_mask(im)
#image_hist(im)
#bar_show(im)
cv2.waitKey() & 0xff
cv2.destroyAllWindows()
