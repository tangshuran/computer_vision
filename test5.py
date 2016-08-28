import harris
from PIL import Image
from matplotlib.pyplot import *
from numpy import *
import cv2
wid = 10
im1=np.array(Image.open("left.png").convert("L"))
im2=np.array(Image.open("right.png").convert("L"))
harrisim = harris.compute_harris_response(im1,5)
filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)
harrisim = harris.compute_harris_response(im2,5)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)
print "starting matching"
e1 = cv2.getTickCount()
matches = harris.match_twosided(d1,d2)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print "matching process takes time:",t, " s"
figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
show()