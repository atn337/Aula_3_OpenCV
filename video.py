# 2. Grave um v�deo;

import numpy as np
import cv2

cap = cv2.VideoCapture("video.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
