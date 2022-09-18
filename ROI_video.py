# 4. Selecione uma ROI (Region of Interest) no vídeo;

import cv2 
import imutils

cap = cv2.VideoCapture("video.mp4"); 

ret, frame1 = cap.read()
ret, frame2 = cap.read()

r = cv2.selectROI(frame1)
frame1 = frame1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

frame2 = frame2[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

while cap.isOpened(): 

  diff = cv2.absdiff(frame1, frame2) 

  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) 

  blur = cv2.GaussianBlur(gray, (5, 5), 0) 

  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) 

  dilated = cv2.dilate(thresh, None, iterations = 3) 

  сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

  for contour in сontours:
    (x, y, w, h) = cv2.boundingRect(contour)

    if cv2.contourArea(contour) < 1000:
      continue
    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    cv2.putText(frame1, "Status: {}".format("Dvijenie is detected!"), (10, 20),     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
    print('Motion Detection. Object area  - ',     cv2.contourArea(contour))
     
  cv2.imshow("WebCamera", frame1)
  frame1 = frame2 
  ret, frame2 = cap.read()   

  if cv2.waitKey(1) == 27: 
    break

cap.release()
cv2.destroyAllWindows()