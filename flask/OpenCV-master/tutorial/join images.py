import cv2
import numpy as np

img = cv2.imread("./face data set/images.jpeg")
img2 = cv2.imread("./face data set/imagefes.jpeg")
# hstack and vstack just can attach two images that completely same as each other.(color , shape, dimension)
himage = np.hstack((img,img,img))
vimage = np.vstack((img,img))

cv2.imshow("Horizontal image",himage)
cv2.imshow("Vertical image",vimage)
cv2.waitKey(0)
