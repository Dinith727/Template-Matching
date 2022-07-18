import cv2 as cv
import numpy as np
img1 = cv.imread('Src/1.jpg',0)
img2 = cv.imread('Src/5.jpg',0)
ret, thresh = cv.threshold(img1, 127, 255,0)
ret, thresh2 = cv.threshold(img2, 127, 255,0)
thresh3 = cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)


contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
contours,hierarchy = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt2 = contours[0]
ret = cv.matchShapes(cnt1,cnt2,1,0.0)
print( ret )

cv.drawContours(img1, contours, 0, (127, 255,0), 3)
cv.imshow('1',thresh2)
cv.drawContours(img2, contours, 0, (127, 255,0), 3)
cv.imshow('2',thresh)

cv.waitKey(0)