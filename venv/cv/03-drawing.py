import numpy as np
import cv2 as cv

#Create a black image
img = np.zeros((512,512,3),np.uint8)



font = cv.FONT_HERSHEY_SIMPLEX

#Drawing line
img = cv.line(img,(0,0),(511,511),(255,0,0),5)
#Drawing rectangle
img = cv.rectangle(img,(0,0),(511,511),(0,255,3),3)
#Drawing cricle
img = cv.circle(img,(200,163),63,(0,0,255),-1)

cv.putText(img,'OpenCV',(10,500),font,4,(255,255,255),1,cv.LINE_AA)

cv.imshow('input image', img)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
