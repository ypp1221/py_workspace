import cv2
clicked = False
frame = None
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
        cv2.imwrite('ypp.jpg',frame)

cameraCapture = cv2.VideoCapture(0)

cv2.namedWindow('my window')
cv2.setMouseCallback('my window', onMouse)

print 'showing camera feed'

success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == 255 and (not clicked):
    cv2.imshow('my window', frame)
    success,frame = cameraCapture.read()
cv2.destroyWindow('my window')
cameraCapture.release()