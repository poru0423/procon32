import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np




img=cv2.imread("img.jpg")
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
#plt.show()
ar=np.array(img)
size=80
sp=np.array([1280,1280,3])
v_size = img.shape[0] // size * size
h_size = img.shape[1] // size * size
img = img[:v_size, :h_size]

v_split = img.shape[0] // size
h_split = img.shape[1] // size
out_img = []
[out_img.extend(np.hsplit(h_img, h_split))
    for h_img in np.vsplit(img, v_split)]


sp=[]    
sp.append(out_img[0])

num = np.array([0,0,0])
num_1 = np.array([0,0,0])
for c in range(70,80):
    for j in range(0,80):    
        num += (out_img[0][c][j]-out_img[1][c][j])
num_1=num
for a in range(1,17): #
    for i in range(1,256): 
        for k in range(0,4):   #回転
            out_img[i]=np.rot90(out_img[i],k)
            for c in range(70,80):  #RBG比較
                for j in range(0,80):    
                    num = (out_img[a-1][c][j]-out_img[i][size-c][j])
            if num[0] < num_1[0]:
                 if num[1] < num_1[1]:
                    if num[2] < num_1[2]:
                      num_1=num
                      out_img[a], out_img[i] = out_img[i], out_img[a]
                             

img_1 = np.hstack(out_img[0:15])           
plt.imshow(img_1)
plt.show()