import cv2
import numpy as np


# import image
img = cv2.imread("./face data set/inddex.jpeg")
# grayscaling img
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blure img
# imgBlur = cv2.GaussianBlur(img, (5,5), 0)
imgBlur = cv2.blur(img,(50,5))
# just show edges
imgCanny = cv2.Canny(img,200,200)

# for i in img:
#     print(i)

print(img.shape)
#for dilation and erodation we should use numpy
kernel = np.ones((5,5),np.uint8)
# make heavier version of edges
imgDilation = cv2.dilate(imgCanny,kernel,iterations=5)
# make thinner version of edges. for better sense we input dilated img.
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("img",img)
print(imgGray.shape)
cv2.imshow("gray",imgGray)
cv2.imshow("blur",imgBlur)
cv2.imshow("dilate",imgDilation)
cv2.imshow("erode",imgEroded)
cv2.imshow("canny", imgCanny)
cv2.waitKey(0)
