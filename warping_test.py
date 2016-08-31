from scipy import ndimage
from PIL import Image
from matplotlib.pyplot import *
from numpy import *
import cv2
import os
import homography
#im = array(Image.open("lena.png").convert("L"))
#H = array([[1.4,0.05,-100],[0.05,1,-100],[0,0,1]])
#im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))
#figure()
#gray()
#imshow(im2)
#show()
def image_in_image(im1,im2,tp):
    """ Put im1 in im2 with an affine transformation
    such that corners are as close to tp as possible.
    tp are homogeneous and counter-clockwise from top left. """
    # points to warp from
    m,n = im1.shape[:2]
    fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])
    # compute affine transform and apply
    H = homography.Haffine_from_points(tp,fp)
    im1_t = ndimage.affine_transform(im1,H[:2,:2],
    (H[0,2],H[1,2]),im2.shape[:2])
    alpha = (im1_t > 0)
    return (1-alpha)*im2 + alpha*im1_t
#tp = array([[0,0,1],[0,1000,1],[1000,1000,1],[1000,0,1]]).T
#ee=ginput(4) unter-clockwise from top left
#tp=vstack((ee,[1,1,1,1]))
im1 = array(Image.open("panda.png").convert("L"))
im2 = array(Image.open("tiananmen.jpeg").convert("L"))
tp = array([[66,186,186,66],[245,245,333,333],[1,1,1,1]])
im3 = image_in_image(im1,im2,tp)
figure()
gray()
imshow(im3)
axis("equal")
axis("off")
show()