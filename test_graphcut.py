from scipy.misc import imresize
import graphcut
from scipy.cluster.vq import *
import sift
from numpy import *
from matplotlib.pyplot import *
from PIL import Image
im = array(Image.open("building.png"))[:,:,:3]
im = imresize(im,0.1,interp="bilinear")
size = im.shape[:2]
# add two rectangular training regions
labels = zeros(size)
labels[3:18,3:18] = -1
labels[-18:-3,-18:-3] = 1
# create graph
g = graphcut.build_bayes_graph(im,labels,kappa=1)
# cut the graph
res = graphcut.cut_graph(g,size)
figure()
graphcut.show_labeling(im,labels)
figure()
imshow(res)
gray()
axis("off")
show()