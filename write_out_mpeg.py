import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'MPEG')
fourcc = cv2.cv.CV_FOURCC(*"MPEG")
out = cv2.VideoWriter('output.mpeg',fourcc, 20.0, (640,480))
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame1",frame)
    cv2.imshow("frame2",gray)
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
out.release()
cap.release()
cv2.destroyAllWindows()