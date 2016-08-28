#test openCV
import cv2
#lena=cv2.imread('lena.png')
#cv2.imshow('lena',lena)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
monster=cv2.VideoCapture(r'D:\github\computer_vision/monster.mp4')
monster.isOpened()
while not monster.isOpened():
    cap = cv2.VideoCapture("monster.mp4")
    cv2.waitKey(1000)
    print "Wait for the header"


import numpy as np
import cv2
cap = cv2.VideoCapture(0)
count = 0
while(count < 100):
    # Capture frame-by-frame
    ret, frame = monster.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(80)
    count=count+1
length = int(monster.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
width  = int(monster.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(monster.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
fps    = monster.get(cv2.cv.CV_CAP_PROP_FPS)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


##########################
cap = cv2.VideoCapture(0)
print cap.grab()