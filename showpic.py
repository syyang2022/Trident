import cv2 as cv
import numpy as np

img = cv.imread('D:/DLmode/Data/NEU-DET/JPEGImages/crazing_20.jpg')
point1 = (140, 29)
point2 = (178, 65)

cv.rectangle(img, point1, point2, (0, 255, 0), 2)
cv.namedWindow("img")
cv.imshow("img", img)
cv.waitKey(10000)