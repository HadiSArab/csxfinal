import cv2
import numpy as np

img = cv2.imread("./face data set/imagefes.jpeg")
# dimention of new image
width, height = 190, 30
# (x,y) of points of considered area in main image
pts1 = np.float32([[4,11],[192,66],[2,43],[190,91]])
# corners of new image. be care about ratio
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# reshape selected area to new dimensions
matrix= cv2.getPerspectiveTransform(pts1,pts2)
#  prepare new image with given dimensions
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("img",img)
cv2.imshow("output image",imgoutput)
cv2.waitKey(0)