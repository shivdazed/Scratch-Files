# -*- coding: utf-8 -*-
"""
check email date if any
Created on Sun Jul 25 10:14:00 2021

@author: DELL
"""
##opencv

import cv2
# imread(2 arg) -- location, -1- as it is,1-color,0: b/w
# 255 -w, 0- b
#  r b g
# imshow (2 arg) -- window name, variable of image
# waitKey(infinte = 0)
# resize(2 arg) -- variable of image to be resized, size (w x h)
# split--(variable of image to be splitedd)
# store -- imwrite(2 arg)-- file name, variable of image to be stoted




### Reading the image -- color, b/w
img2=cv2.imread(r'img7_1.jpg',1)
cv2.imshow('cat',img2)
cv2.waitKey(0)
## Read as b/w
img2=cv2.imread(r'C:\Users\DELL\Desktop\cat_image.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('window_name',img2)
cv2.waitKey(0)

##Resize te image
img3=cv2.resize(img2,(1076,512))
b,g,r = cv2.split(img3)
cv2.imshow('cat_BLACWHITE_resized',img3)
cv2.waitKey(0)

## to save the image
cv2.imwrite('cat_resize_bw.jpg',img3)

## Splitting
img4=cv2.imread(r'mirror_dog.jpg',1)
B,G,R = cv2.split(img4)
cv2.imshow('cat_blue',img4)
cv2.waitKey(0)

## aritmatic operation -- same size
iad1=cv2.imread('img6_bw1.png',0)
iad2=cv2.imread('img6_bw2.png',0)

addnimage=cv2.add(iad1,iad2)

cv2.imshow('img_add',addnimage)
cv2.waitKey(0)

iad1=cv2.imread('img6_bw3.png')
iad2=cv2.imread('img6_bw4.png')
addnimage=cv2.subtract(iad1,iad2)
cv2.imshow('img_add',iad2)
cv2.waitKey(0)

# Weightaded addition -- filters

iadw1=cv2.imread('img1.png')
iadw2=cv2.imread('img2.png')

cv2.imshow('img',iadw2);cv2.waitKey(0)


wi=cv2.addWeighted(iadw1,0,iadw2,0.5,0)
cv2.imshow('img_add',wi)
cv2.waitKey(0)

#weighted add ex2 on random images
img2 -- 159 x318x1
img4_r --

img4_r=cv2.resize(img4,(318,159))

adw=cv2.addWeighted(img2, 0.5, img4_r, 0.5, 0)
cv2.imshow('img_add',adw)
cv2.waitKey(0)
# Task ends here

dog_resize=cv2.resize(b,(800,599))
wi=cv2.addWeighted(img2,0.4,dog_resize,0.6,0)
cv2.imshow('img_add',img4)
cv2.waitKey(0)

dog_resize=cv2.resize(img4,(800,599))
wi=cv2.addWeighted(img1,0.4,dog_resize,0.6,0)
cv2.imshow('img_add',wi)
cv2.waitKey(0)

iadw1=cv2.imread('img7_1.jpg')
iadw2=cv2.imread('img7_2.jpg')
cv2.imshow('img_add',iadw1);cv2.waitKey(0)
new_i=cv2.resize(iadw1,(513,159))
wi=cv2.addWeighted(iadw2,0.4,new_i,0.6,0)
cv2.imshow('img_add',wi)
cv2.waitKey(0)
## Geometry
cv2.line(img4, (0,40),(1000,40),(50,0,255),1)
cv2.imshow('img_add',img4)
# cv2.rectangle(img4,(300,500),(500,700),(21,136,25),4)
# cv2.putText(img4,'Roger',(300,400),cv2.FONT_ITALIC,2,(255,0,0),4)

a=cv2.waitKey(0)
if a == ord('q'):
    cv2.destroyAllWindows()


## fliping an image
flip_img=cv2.flip(img2,-1);
cv2.imshow('img_add',img4_r);cv2.waitKey(0)

# Concatinating images
h=cv2.hconcat([flip_img,img2])
v=cv2.vconcat([flip_img,img2])

mirror=cv2.hconcat([img4,flip_img])
cv2.imwrite('mirror_dog.jpg',mirror)
cv2.imshow('img_add',mirror);cv2.waitKey(0)

bl=cv2.blur(img4,(15,15))
cv2.imshow('img_add',bl);cv2.waitKey(0)
gblr = cv2.GaussianBlur(img4,(7,7),0)
cv2.imshow('img_add',bl);cv2.imshow('img_add1',gblr);cv2.waitKey(0)

## edge detection
bl_cat_bw=cv2.blur(img4,(7,7))
ed_cat=cv2.Canny(bl_cat_bw, 70,100)
cv2.imshow('img_add1',ed_cat);cv2.waitKey(0)

ed_cat=cv2.Canny(bl_cat_bw, 90, 130)
cv2.imshow('img_add1',ed_cat);cv2.waitKey(0)


face_img=cv2.imread('NeelamPic.png',0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_=face_cascade.detectMultiScale(face_img,2,3)
print(face_)
for (x,y,w,h) in face_:
    cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow('test_run',face_img);cv2.waitKey(0)
