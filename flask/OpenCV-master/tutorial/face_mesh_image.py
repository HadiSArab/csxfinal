import mediapipe as mp
import time
import cv2
import json

# for create a dictionary from values and store in json file
def xy(x , y):
    yield{
        " x " : x,
        " y " : y
    }

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
d = {}

img = cv2.imread("D:\python\scraper\OpenCV\\tutorial\\face data set\happyface\\5.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceMesh.process(imgRGB)
if results.multi_face_landmarks:
    for faceLms in results.multi_face_landmarks:
        mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS,drawSpec,drawSpec) #FACE_CONNECTION replaced by FACEMESH_CONTOURS
    for id,lm in enumerate(faceLms.landmark):
        #print(lm)
        ih, iw, ic = img.shape
        x,y = int(lm.x*iw), int(lm.y*ih)
        print(id,x,y)

        # store values in a dictionary and then in json file 
        temp = xy(x , y)
        for i in temp:
            d[id]=i
 
with open ("face data set/output_images/5.json","w") as file:
    json.dump(d , file)
    
cv2.imwrite("face data set/output_images/5.jpg",img)
cv2.imshow("Image", img)
cv2.waitKey(0)
