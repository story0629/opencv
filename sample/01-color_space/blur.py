import cv2
import numpy as np

img = cv2.imread("lena.jpg")

cv2.namedWindow("Gaussian_Blur")
cv2.createTrackbar("ksize","Gaussian_Blur",0,10,nothing)

with True:
    ksize = cv2.getTrackbarPos("ksize","Gaussian_Blur")
    blur = cv2.GaussianBlur(img,(2*ksize+1,2*ksize+1),0)
    cv2.imshow("Gaussian_Blur",blur)