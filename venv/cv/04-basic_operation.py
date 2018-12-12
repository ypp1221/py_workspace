import cv2
import numpy as np
import  time
im = cv2.imread('../image/houzi.jpg',1)

print im[300,250]
print im.item(300,250,0)
im.itemset((300,250,0),100)
print im[300,250,0]
ball = im[0:300,300:500]
print ball.shape
im[0:300,0:200] = ball
cv2.imshow('houzi',im)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
