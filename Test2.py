import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('Src/4.1.jpg',0)
img2 = cv.imread('Src/4.jpg',0)

edges1 = cv.Canny(img1,100,200)
edges2 = cv.Canny(img2,100,200)

contours,hierarchy = cv.findContours(edges1, 2,1)
cnt1 = contours[0]
contours2,hierarchy = cv.findContours(edges2, 2,1)
cnt2 = contours2[0]

ret = cv.matchShapes(cnt1,cnt2,1,0.0)
ret2 = cv.matchShapes(edges1,edges2,1,0.0)
# res = cv.matchTemplate(edges1,edges2,cv.TM_SQDIFF)

print( 'ret' )
print( ret )
print( 'ret2' )
print( ret2 )
# print( 'res' )
# print( res )

# cv.drawContours(thresh, contours, 0, (127, 255,0), 3)
cv.imshow('1',edges1)
# cv.drawContours(thresh2, contours, 0, (127, 255,0), 3)
cv.imshow('2',edges2)

cv.waitKey(0)

# kernel1x = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
# kerne1ly = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
# img1_prewittx = cv.filter2D(img_gaussian, -1, kernelx)
# img1_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

# plt.subplot(121),plt.imshow(img1,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges1,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()