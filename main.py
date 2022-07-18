import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('Src/2D_Simple_Shapes-01.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('Src/5.jpg',0)
template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',img_rgb)
cv.imshow('res1.png',img_rgb)

cv.waitKey(0)

ret = cv.matchShapes(img_rgb, template_gray, 1, 0.0)
print( ret )
print( 'ret' )