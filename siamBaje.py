import string
from PIL import Image
import numpy as NP
import os
import glob
import time

skin_pix_count = NP.zeros([256,256,256])
non_skin_pix_count = NP.zeros([256,256,256])
# probability_skin = [[[0]*256]*256]*256
# probability_non_skin = [[[0]*256]*256]*256
total_skin = 0
total_non_skin = 0 
 
start_time = time.time()
 
images = sorted(glob.glob('images\*.jpg'))
masks = sorted(glob.glob('Mask\*.bmp'))

 
for i in range (0, len(images)):
    img = Image.open(images[i])
    mask = Image.open(masks[i])
    pixel_img = img.load()
    pixel_mask = mask.load()
    # print(i)
    for y in range (0, mask.size[1]):
        for x in range (0, mask.size[0]):
            if pixel_mask[x,y][0] < 255 or pixel_mask[x,y][1] < 255 or pixel_mask[x,y][2] < 255:
                skin_pix_count[pixel_img[x,y][0]][pixel_img[x,y][1]][pixel_img[x,y][2]] += 1
                total_skin += 1
            else:
                non_skin_pix_count[pixel_img[x,y][0]][pixel_img[x,y][1]][pixel_img[x,y][2]] += 1
                total_non_skin += 1

f= open('siamabal.txt', 'w') 
      
for r in range(0,256):
    for g in range(0,256):
        for b in range(0,256):
            skin_pix_count[r][g][b] = skin_pix_count[r][g][b]/total_skin
            non_skin_pix_count[r][g][b] = non_skin_pix_count[r][g][b]/total_non_skin
            if(non_skin_pix_count[r][g][b]==0):
                prob=min(skin_pix_count[r][g][b],1)
            else:
                prob=skin_pix_count[r][g][b]/non_skin_pix_count[r][g][b]

                # print(proSkin[r][g][b])
            f.write(str(prob)+"\n")
f.close()
print("--- %s seconds ---" % (time.time() - start_time))