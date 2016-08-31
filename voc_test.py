import pickle
import vocabulary
import glob
import os
from numpy import *
from matplotlib.pyplot import *

os.chdir("D:\Achive\ukbench\samples")
imlist=glob.glob("*.jpg")
nbr_images = len(imlist)
featlist = [ imlist[i][:-3]+"sift" for i in range(nbr_images) ]
voc = vocabulary.Vocabulary("ukbenchtest")
voc.train(featlist,990,10)
# saving vocabulary
with open("vocabulary.pkl", "wb") as f:
    pickle.dump(voc,f)
print "vocabulary is:", voc.name, voc.nbr_words