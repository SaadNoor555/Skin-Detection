# IS NOT CORRECT
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
nskin = NP.zeros([256,256,256])
proSkin=NP.zeros([256,256,256])

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
        else:
            nskin[pixel1[0]][pixel1[1]][pixel1[2]]+=1
            # print("hi")
f= open('dataBad.txt', 'w') 

for r in range(0,256):
    for g in range(0,256):
        for b in range(0,256):
            if(cnt[r][g][b]+nskin[r][g][b]!=0):
                proSkin[r][g][b]= cnt[r][g][b]/(cnt[r][g][b]+nskin[r][g][b])
                # print(proSkin[r][g][b])
            f.write(str(proSkin[r][g][b])+"\n")

f.close()           
print("--- %s seconds ---" % (time.time() - start_time))
