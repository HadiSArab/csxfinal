import cv2
import numpy as np
import mediapipe as mp
import time
import json
import glob

class img_editor:
    
    def rot(img, angle):
        y,x,ht= img.shape
        matrix= cv2.getRotationMatrix2D((x/2,y/2),angle,1)
        rot = cv2.warpAffine(img, matrix, (x,y))
        return rot

    def crop(img,x1,x2,y1,y2):
        imgcropped = img[y1:y2,x1:x2]
        return imgcropped

    def color_detector(img,h_min,h_max,s_min,s_max,v_min,v_max):
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])

        imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
        
        mask = cv2.inRange(imgHSV,lower,upper)
        imgmask = cv2.bitwise_and(img,img,mask=mask)
        
        return imgmask
        
    def create_shape(size, color):
        img = np.zeros((size[0],size[1],3),np.uint8)
        img[0:size[0],0:size[1]] = color[0],color[1],color[2]
        return img
    
    def put_shape_on_image(img, size, color, start_point):
        img[start_point[1]:(start_point[1]+size[1]),start_point[0]:(start_point[0]+size[0])] = color[0],color[1],color[2]
        return img
    
    def creat_video(path,video_name,images_type):
        frameSize = (264, 148)

        out = cv2.VideoWriter(str(path)+'\\'+str(video_name)+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, frameSize)

        for filename in glob.glob(str(path)+'\*.'+str(images_type)):
            img = cv2.imread(filename)
            out.write(img)

        out.release()
    
    def extract_frames(video_path,out_folder):

        # Opens the inbuilt camera of laptop to capture video.
        cap = cv2.VideoCapture(video_path)
        
        success, image = cap.read()
        frame_count = 0
        # cv2.imshow("ali",image)
        while success:
            cv2.imwrite(f"{out_folder}/frame_{frame_count}.jpg", image)
            success, image = cap.read()
            frame_count += 1
        
        cap.release()
                


class face_detection:
    def find_face(path):
        cap = cv2.VideoCapture(path)
 
        pTime = 0
        mpFaceDetection = mp.solutions.face_detection
        mpDraw = mp.solutions.drawing_utils
        faceDetection = mpFaceDetection.FaceDetection(0.75)                            # by default (0.5) and you can change it for accuracy
        while True:
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = faceDetection.process(imgRGB)
            # print(results)

            if results.detections:
                for id , detection in enumerate(results.detections):
                    print(id, detection)
                    # print(detection.score)                                           # its subvalue of detection
                    # print(detection.location_data.relative_bounding_box)             #its show how get sub data's
                    # mpDraw.draw_detection(img, detection)                            #draw face area and key points on show images
                    
                    # draw rectangle on face with our own formula
                    bboxC = detection.location_data.relative_bounding_box
                    ih , iw , ic = img.shape
                    bbox = int (bboxC.xmin * iw), int(bboxC.ymin * ih), int (bboxC.width * iw) , int(bboxC.height * ih) 
                    cv2.rectangle(img, bbox , (0,0,255),2)
                    cv2.putText(img, f'{int(detection.score[0] * 100)} %', (int(bboxC.xmin * iw),int ((bboxC.ymin * ih)- 20)), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,0), 1)

            
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime
            cv2.putText(img , f'FPS : {int (fps)}' ,(10,30), cv2.FONT_HERSHEY_COMPLEX , .5 , (255,100,0) , 1 )
            cv2.imshow("image",img)
            cv2.waitKey(10)

    def face_mesh_video(path, max_faces,thick,circle_rad):

        cap = cv2.VideoCapture(path)
        pTime = 0
        
        mpDraw = mp.solutions.drawing_utils
        mpFaceMesh = mp.solutions.face_mesh
        faceMesh = mpFaceMesh.FaceMesh(max_num_faces=max_faces) #dedpend on number of faces that you want to detect. normally is 2
        drawSpec = mpDraw.DrawingSpec(thickness=thick, circle_radius=circle_rad) #by default both are 1

        while True:
            success, img = cap.read()
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
        
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
            3, (255, 0, 0), 3)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
    
    def face_mesh_image(img, max_faces,thick,circle_rad):
        
        # for create a dictionary from values and store in json file
        def xy(x , y):
            yield{
                " x " : x,
                " y " : y
            }

        mpDraw = mp.solutions.drawing_utils
        mpFaceMesh = mp.solutions.face_mesh
        faceMesh = mpFaceMesh.FaceMesh(max_num_faces=max_faces)
        drawSpec = mpDraw.DrawingSpec(thickness=thick, circle_radius=circle_rad)
        d = {}


        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceMesh.process(imgRGB)
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS,drawSpec,drawSpec) #FACE_CONNECTION replaced by FACEMESH_CONTOURS
            for id,lm in enumerate(faceLms.landmark):
                #print(lm)
                ih, iw, ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                # print(id,x,y)

                # store values in a dictionary and then in json file 
                temp = xy(x , y)
                for i in temp:
                    d[id]=i
        
        return img