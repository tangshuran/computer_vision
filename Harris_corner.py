from scipy.ndimage import filters
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.pyplot import *
def compute_harris_response(im,sigma=3):
    """Compute the Harris corner detector response function
       for each pixel in a graylevel image."""
    imx = np.zeros(im.shape)
    filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)
    imy = np.zeros(im.shape)
    filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)
    # compute components of the Harris matrix
    Wxx = filters.gaussian_filter(imx*imx,sigma)
    Wxy = filters.gaussian_filter(imx*imy,sigma)
    Wyy = filters.gaussian_filter(imy*imy,sigma)
    # determinant and trace
    Wdet = Wxx*Wyy - Wxy**2
    Wtr = Wxx + Wyy
    return Wdet / Wtr
def get_harris_points(harrisim,min_dist=10,threshold=0.1):
    """ Return corners from a Harris response image
    min_dist is the minimum number of pixels separating
     corners and image boundary"""
    # find top corner candidates above a threshold
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1
    # get coordinates of candidates
    coords = np.array(harrisim_t.nonzero()).T
    # ...and their values
    candidate_values = [harrisim[c[0],c[1]] for c in coords]
    # sort candidates
    index = np.argsort(candidate_values)
    # store allowed point locations in array
    allowed_locations = np.zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist,min_dist:-min_dist] = 1
    # select the best points taking min_distance into account
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i,0],coords[i,1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),
            (coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0
    return filtered_coords
def plot_harris_points(image,filtered_coords):
    """ Plots corners found in image. """
    figure()
    gray()
    imshow(image)
    plot([p[1] for p in filtered_coords],[p[0] for p in filtered_coords],"*")
    axis("off")
    show()
img = cv2.imread('lena.png')
img_gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY )
harris=compute_harris_response(img_gray,sigma=2)
#cv2.imshow("harris1",compute_harris_response(img_gray,sigma=1))
#cv2.imshow("harris2",compute_harris_response(img_gray,sigma=2))
#cv2.imshow("harris3",compute_harris_response(img_gray,sigma=3))
#cv2.imshow("gray",img_gray)
im = np.array(Image.open("lena.png").convert("L"))
harrisim = compute_harris_response(im)
filtered_coords = get_harris_points(harrisim,6)
plot_harris_points(im, filtered_coords)