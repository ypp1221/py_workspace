import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
#为0时是打开摄像头，当出入.avi文件时直接写入路径就行
while(cap.isOpened()):
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2BGRA)

    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()