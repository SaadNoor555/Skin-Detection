# TESTER CODE
from fileinput import filename
import numpy as NP
from PIL import Image
import os
from pathlib import Path
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


start_time = time.time()

tc= 0.3
proSkin=NP.zeros([256,256,256])

f= open('siamabal.txt', 'r')
for r in range(0,256):
    for g in range(0,256):
        for b in range(0,256):
            proSkin[r][g][b] = float(f.readline())





im1= Image.open('siamtest1.png')
wid,hig= im1.size
# print(wid)
# print(hig)

o_img = Image.new(mode="RGB", size=im1.size)
pixel_map = o_img.load()



for x in range (0, wid):
    for y in range (0, hig):
        pix = im1.getpixel((x,y))
        if(proSkin[pix[0]][pix[1]][pix[2]]<tc):
            pixel_map[x,y]= 0,0,0
        else:
            pixel_map[x,y]= pix[0], pix[1], pix[2]
# print(cnt)
f.close()
o_img.save('siamtestres1.png')
o_img.show()
im1.show()
print("--- %s seconds ---" % (time.time() - start_time))