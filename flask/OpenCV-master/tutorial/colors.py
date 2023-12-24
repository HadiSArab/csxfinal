import cv2
import numpy as np

# "np.zeros" make an array with "0" value
# "512,512,3" define array x, y, z . 3 chanel for RGB color value
# np.uint8 convert "addade ashare" be "addade sahih"
img = np.zeros((512,512,3),np.uint8)
print(img.shape)

# define channels colors, "img[:] = " meanes all subs of array get new value
# also we can select an area from image to change color with "img[100:200,150,450]" : from line 100 to 200 and from column 150 to 450
img[50:450,130:250] = 125,125,125

# "imshow" undrestand array and convert it to visible image
cv2.imshow("img",img)
cv2.waitKey(0)
