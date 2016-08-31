from PIL import Image
from matplotlib.pyplot import *
from numpy import *
import cv2
import os
import sift
import glob
os.chdir("D:\Achive\ukbench\samples")
imlist=glob.glob("*.jpg")
for file in imlist:
    sift.process_image(file,os.path.splitext(file)[0]+".sift")
#os.chdir("..")   
#sift.process_image("ukbench00082.jpg","ukbench00082.sift")