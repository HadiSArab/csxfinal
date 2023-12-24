import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# cv2.line(target image name, start point, end point, color, thickness)
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,0,255),3)
# cv2.rectangle(image name, start point(up left corner), endpoint(down right corner), color, thickness(also can fill) )
cv2.rectangle(img,(100,100),(200,200),(150,0,0),cv2.FILLED)
# cv2.circle(image name, origin, radius, color, thickness)
cv2.circle(img,(250,50),30,(0,100,100),2)
# cv2.putText(image name, text, start point, font, scale(accept decimal for instance:0.5), color, thickness)
cv2.putText(img,"salam",(100,400),cv2.FONT_HERSHEY_COMPLEX,1,(250,250,250),1)

cv2.imshow("img",img)
cv2.waitKey(0)