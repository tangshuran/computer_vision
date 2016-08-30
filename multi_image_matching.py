from PIL import Image
from matplotlib.pyplot import *
from numpy import *
import cv2
import os
import sift
import glob
import pydot
os.chdir("./panoramio_pictures")
imlist=glob.glob("*.jpg")
featlist=glob.glob("*.sift")
nbr_images = len(imlist)
matchscores = zeros((nbr_images,nbr_images))
for i in range(nbr_images):
    for j in range(i,nbr_images): # only compute upper triangle
        print "comparing ", imlist[i], imlist[j]
        l1,d1 = sift.read_features_from_file(featlist[i])
        l2,d2 = sift.read_features_from_file(featlist[j])
        matches = sift.match_twosided(d1,d2)
        nbr_matches = sum(matches > 0)
        print "number of matches = ", nbr_matches
        matchscores[i,j] = nbr_matches
# copy values
for i in range(nbr_images):
    for j in range(i+1,nbr_images): # no need to copy diagonal
        matchscores[j,i] = matchscores[i,j]

########### multi pictures graph illustration
threshold = 2 # min number of matches needed to create link
g = pydot.Dot(graph_type="graph") # don"t want the default directed graph
path=r"D:\github\computer_vision\panoramio_pictures/"
for i in range(nbr_images):
    for j in range(i+1,nbr_images):
        if matchscores[i,j] > threshold:
            #first image in pair
            im = Image.open(imlist[i])
            im.thumbnail((100,100))
            filename = str(i)+".png"
            im.save(filename) # need temporary files of the right size
            g.add_node(pydot.Node(str(i),fontcolor="transparent",shape="rectangle",image=path+filename))
            # second image in pair
            im = Image.open(imlist[j])
            im.thumbnail((100,100))
            filename = str(j)+".png"
            im.save(filename) # need temporary files of the right size
            g.add_node(pydot.Node(str(j),fontcolor="transparent",shape="rectangle",image=path+filename))
            g.add_edge(pydot.Edge(str(i),str(j)))
g.write_png("whitehouse.png")        
