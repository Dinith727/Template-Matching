import cv2 as cv
import numpy as np
img1 = cv.imread('Src/5.jpg',0)
img2 = cv.imread('Src/5.jpg',0)
# ret, thresh = cv.threshold(img1, 127, 255,0)
# ret, thresh2 = cv.threshold(img2, 127, 255,0)

blur = cv.GaussianBlur(img1,(5,5),0)
ret,thresh = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

blur2 = cv.GaussianBlur(img2,(5,5),0)
ret,thresh2 = cv.threshold(blur2,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# thresh = cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,11,2)
# thresh2 = cv.adaptiveThreshold(img2,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,11,2)

cnt3 = cv.connectedComponents(thresh)
cnt4 = cv.connectedComponents(thresh2)

contours,hierarchy = cv.findContours(thresh, 2,1)
cnt1 = contours[0]
contours2,hierarchy = cv.findContours(thresh2, 2,1)
cnt2 = contours2[0]

ret = cv.matchShapes(cnt1,cnt2,1,0.0)
res = cv.matchTemplate(thresh,thresh2,cv.TM_CCOEFF_NORMED)
#ret2 = cv.matchShapes(cnt3,cnt3,1,0.0)
# ret3 = cv.matchShapes(img1,img2,1,0.0)
# print('cnt1')
# print(cnt1)
# print('cnt2')
# print(cnt2)
# print( 'cnt3' )
print( cnt3 )
print( cnt4 )
print( 'ret' )
print( ret )
print( 'res' )
print( res )
# print( 'ret2' )
# print( ret2 )
# if ret != 0.00000:
#     print(ret)
# elif ret != 0.00000:
#     print(ret2)
# else :
#     print(ret3)


# cv.drawContours(thresh, contours, 0, (127, 255,0), 3)
cv.imshow('1',thresh)
# cv.drawContours(thresh2, contours, 0, (127, 255,0), 3)
cv.imshow('2',thresh2)

cv.waitKey(0)