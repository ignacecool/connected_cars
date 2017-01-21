import numpy as np
import cv2

# setup video capture
cap = cv2.VideoCapture(0)
ret,im = cap.read()


gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


height, width = im.shape[:2]
print height
print width

while True:
    ret,im = cap.read()

    # Blur image to remove noise
#    img_filter = cv2.GaussianBlur(im.copy(), (3, 3), 0)
    
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #retval, threshold = cv2.threshold(im, 12, 255, cv2.THRESH_BINARY)

    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


    cv2.imshow('My camera' ,im)
    cv2.imshow('Binary camera', th)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
