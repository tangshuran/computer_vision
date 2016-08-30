from PIL import Image
from matplotlib.pyplot import *
from numpy import *
import cv2
import os
import sift
imname1 = "left_dark.png"
im1 = array(Image.open(imname1).convert("L"))
sift.process_image(imname1,"left.sift")
l1,d1 = sift.read_features_from_file("left.sift")
imname2 = "right.png"
im2 = array(Image.open(imname2).convert("L"))
sift.process_image(imname2,"right.sift")
l2,d2 = sift.read_features_from_file("right.sift")
gray()
matches = sift.match_twosided(d1,d2)
sift.plot_matches(im1,im2,l1,l2,matches)
#sift.plot_features(im1,l1,circle=True)
show()