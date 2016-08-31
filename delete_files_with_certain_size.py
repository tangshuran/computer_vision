import os
import glob
os.chdir("D:\Achive\ukbench\samples")
filelist=glob.glob("*.sift")
for file in filelist:
    if os.stat(file).st_size<2000:
        os.remove(file)
        os.remove(file[:-4]+"jpg")

