import cv2
import numpy as np

#scaling and resizing
# in opencv (0.0) or original or refrence point is top left of the img

img = cv2.imread("./face data set/images.jpeg")
# resize func: (lenght,hight)
imgResize = cv2.resize(img,(750,500))
# crop func: [from height: to height , from lengh : to lengh]
imgCropped = imgResize[0:200,250:750]
# print size of img: (Height, lenght, number of RGB chanels)
print(img.shape)
print("resized = ",imgResize.shape)
print("cropped = ",imgCropped.shape)

cv2.imshow("show",img)
cv2.imshow("resize",imgResize)
cv2.imshow("cropped",imgCropped)
cv2.waitKey(0)
