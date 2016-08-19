import cv2
import numpy as np
#img = np.zeros((512,512,3), np.uint8)
#cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#cv2.circle(img,(447,63), 20, (0,0,255),-1)
#font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img,'OpenCV',(10,500), font, 3,(255,255,255),4,cv2.CV_AA)
#cv2.imshow("image",img)
#lena=cv2.imread("lena.png",cv2.COLORMAP_PINK)
#cv2.imshow("lena",lena)
left=cv2.imread("left.png")
right=cv2.imread("right.png")
add=cv2.add(left/2,right/2)
cv2.imshow("add",add)
cv2.waitKey(0)
cv2.destroyAllWindows()