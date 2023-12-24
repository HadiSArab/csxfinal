import cv2
import numpy as np

def empty(a):
    pass


# we make a window in size of 640 , 240 to put scroll editors in it 
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

# scroles for editing image. we have 6 variable for controlling all image color variation.
# oonayi ke az 0 shoro mishe b onayi ke az max shoro mishe fargheshon jaye default scroll ast. e.g onike ro 179 ast default az 179 shoro mishe
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)                  
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

#reading trackbar values and stor in variables
while True:
    img = cv2.imread('/home/python/PycharmProjects/OpenCV/tutorial/face data set/3cars.jpeg')

    # convert from RGB to HSV to be able to edit and detect multi range of colors
    # HSV format have three argument: value (Brightness) , hue (colors), Saturation
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    v_max = cv2.getTrackbarPos("Val Max","Trackbars")
    
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    # generate an array of lower and higher range of values
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    # generate a mask with desired values (choosen in trackbar)
    mask = cv2.inRange(imgHSV,lower,upper)
    
    # put the mask on main image and make new image
    imgmask =cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("hsv", imgHSV)
    cv2.imshow("main", img)
    cv2.imshow("mask",imgmask)
    cv2.waitKey(1)
