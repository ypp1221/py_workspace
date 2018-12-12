import cv2

img = cv2.imread('../image/car.jpg')

cv2.imshow('my image', img)
key = cv2.waitKey(1)
if key != -1:
    key &= 0xFF
print key
cv2.destroyAllWindows()
