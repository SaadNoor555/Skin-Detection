# TRAINER CODE SKAIB
from fileinput import filename
import numpy as NP
from PIL import Image
import os
from pathlib import Path
import time

start_time = time.time()

directory1= "Mask"
directory= "images"
# files= Path(directory).glob('*')
files1= Path(directory1).glob('*')

skin= NP.zeros([256,256,256])
nskin = NP.zeros([256,256,256])
# proSkin=NP.zeros([256,256,256])
# proNonSkin=NP.zeros([256,256,256])
# skinCount=0
# nonSkinCount=0

for fname in files1: 
    im = Image.open(fname)
    filename= im.filename
    newf= filename[54:-3]
    newf= directory + "/" + newf+ "jpg"
    ims= Image.open(newf)

    for (pixel, pixel1) in zip(im.getdata(),ims.getdata()):
        # if pixel[0]==pixel1[0] and pixel[1]==pixel1[1] and pixel[2]==pixel1[2] and (pixel[0]<255 or pixel[1]<255 or pixel[2]<255):
        if  (pixel[0]<255 or pixel[1]<255 or pixel[2]<255):
            skin[pixel1[0]][pixel1[1]][pixel1[2]]+=1
            # skinCount+=1
        else:
            nskin[pixel1[0]][pixel1[1]][pixel1[2]]+=1
            # nonSkinCount+=1
f= open('saad1.txt', 'w') 

for r in range(0,256):
    for g in range(0,256):
        for b in range(0,256):
            if(nskin[r][g][b]==0):
                prob=min(skin[r][g][b],1)
            else:
                prob = skin[r][g][b]/nskin[r][g][b]

                # print(proSkin[r][g][b])
            f.write(str(prob)+"\n")

f.close()           
print("--- %s seconds ---" % (time.time() - start_time))
