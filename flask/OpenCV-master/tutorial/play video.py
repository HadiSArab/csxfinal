import cv2

# play a video
cap = cv2.VideoCapture("./face data set/1.mp4")
while True:
    success, img=cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

