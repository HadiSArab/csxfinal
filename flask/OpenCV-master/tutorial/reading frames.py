import cv2
import time

# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture("/home/python/PycharmProjects/OpenCV/tutorial/face data set/2.mp4")
 
success, image = cap.read()
frame_count = 0
# cv2.imshow("ali",image)
while success:
    cv2.imwrite(f"extracted_images/frame_{frame_count}.jpg", image)
    success, image = cap.read()
    frame_count += 1
 
cap.release()