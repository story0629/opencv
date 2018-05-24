import numpy as np
import cv2
import sys 

path = sys.argv[1]
img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
(contrours,_)=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(127,127,255),3)
cv2.imshow("Contours",img)