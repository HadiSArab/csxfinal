import cv2

img = cv2.imread("D:\python\scraper\OpenCV\\tutorial\\face data set\\alikhani1.jpeg")
x,y,ht = img.shape
# print(img.shape())
matrix = cv2.getRotationMatrix2D((x/2,y/2),90,1)
new_img = cv2.warpAffine(img,matrix,(x,y))

cv2.imshow("image",new_img)
cv2.waitKey(0)
