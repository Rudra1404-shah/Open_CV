import cv2
import numpy as np
flags =  False
ix = -1
iy = -1
def draw(event,x,y,flag,param):
    global flags , ix,iy , img
    if event == cv2.EVENT_LBUTTONDOWN:

        flags  = True
        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE:

        if flags:
            temp = img.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
            cv2.imshow("Image", temp)
    elif event == cv2.EVENT_LBUTTONUP:
        flags = False
        fx = x
        fy = y
        temp = img.copy()
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
        cv2.imshow("Image", temp)
        temp_value  = temp[iy:fy, ix:fx]
        cv2.imshow("Image",temp_value)
        cv2.namedWindow('image_NewWindow')
        cv2.waitKey(0)
img = cv2.imread('download (3).jpg')

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cv2.destroyAllWindows()