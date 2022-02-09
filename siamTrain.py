# TRAINER CODE
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
cnt= NP.zeros([256,256,256])
print(type(cnt))
nskin = NP.zeros([256,256,256])
proSkin=NP.zeros([256,256,256])
proNonSkin=NP.zeros([256,256,256])
skinCount=0
nonSkinCount=0

for fname in files1:
    im = Image.open(fname)
    filename= im.filename
    newf= filename[54:-3]
    newf= directory + "/" + newf+ "jpg"
    ims= Image.open(newf)

    for (pixel, pixel1) in zip(im.getdata(),ims.getdata()):
        if pixel[0]==pixel1[0] and pixel[1]==pixel1[1] and pixel[2]==pixel1[2] and (pixel[0]<250 or pixel[1]<250 or pixel[2]<250):
            # print("hello")
            cnt[pixel1[0]][pixel1[1]][pixel1[2]]+=1
            skinCount+=1
        else:
            nskin[pixel1[0]][pixel1[1]][pixel1[2]]+=1
            nonSkinCount+=1
            # print("hi")
f= open('datas.txt', 'w') 

prob=0
for r in range(0,256):
    for g in range(0,256):
        for b in range(0,256):
            if(skinCount!=0):
                proSkin[r][g][b]= cnt[r][g][b]/skinCount
            if(nonSkinCount!=0):
                proNonSkin[r][g][b]= nskin[r][g][b]/nonSkinCount
            if(proNonSkin[r][g][b]==0):
                prob=1
            else:
                prob=proSkin[r][g][b]/proNonSkin[r][g][b]

                # print(proSkin[r][g][b])
            f.write(str(prob)+"\n")

f.close()           
print("--- %s seconds ---" % (time.time() - start_time))