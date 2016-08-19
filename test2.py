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
#add
#left=cv2.imread("left.png")
#right=cv2.imread("right.png")
#add=cv2.add(left/2,right/2)
#cv2.imshow("add",add)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#add logo
img1 = cv2.imread('panda2.jpg')
img2 = cv2.imread('opencv.jpg')
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
