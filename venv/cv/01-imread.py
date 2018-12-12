#coding=utf-8
import numpy as np
import cv2
"""
im = cv2.imread(,);

1 第一个参数为图像路径
路径错误时不会返回错误，返回结果为None
2 第二个参数为读入图像的格式
    cv2.IMREAD_COLOR  : 读入彩色图像 对应数字 1
    cv2.IMREAD_GRAYSCALE: 读入灰度图片 0
    cv2.IMREAD_UNCHANGED : -1

"""

im = cv2.imread('../image/houzi.jpg',0)
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow('input image', im)
k = cv2.waitKey(0) & 0xff
if k == 27: #wait for esc key to eixt
    #Esc 键对应着键盘27
    print k
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('../image/new_houzi.jpg',im)
    cv2.destroyAllWindows()
