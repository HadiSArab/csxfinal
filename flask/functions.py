from rembg import remove
from PIL import Image
import cv2
import numpy as np
import mediapipe as mp


class img_editor:
    
    def rmbg(photo,filename):
        output_path = './export/{}_rmbg.jpg'
        output_path = output_path.format(filename)

        input = Image.open(photo)
        output = remove(input)
        
        output.save(output_path) 
        return output_path

# ................................................................angle ask from user
    def rot(photo,filename, angle):
        y,x,ht= photo.shape
        matrix= cv2.getRotationMatrix2D((x/2,y/2),angle,1)
        output = cv2.warpAffine(photo, matrix, (x,y))
        
        output_path = './export/{}_rot{}.jpg'
        output_path = output_path.format(filename,angle)
        
        output.save(output_path) 
        return output_path

#............................................................. crop points show in image
    def crop(photo,filename,x1,x2,y1,y2):
        output = photo[y1:y2,x1:x2]
        
        output_path = './export/{}_crop.jpg'
        output_path = output_path.format(filename)
        
        output.save(output_path) 
        return output_path


    def resize(photo,filename,width, height):
        # resize func: (lenght,hight)
        output = cv2.resize(photo,(width, height))
        
        output_path = './export/{}_resize.jpg'
        output_path = output_path.format(filename)
        
        output.save(output_path) 
        return output_path


class face_detection:
    def find_face(photo,filename):
 
        
        mpFaceDetection = mp.solutions.face_detection
        mpDraw = mp.solutions.drawing_utils
        faceDetection = mpFaceDetection.FaceDetection(0.75)                            # by default (0.5) and you can change it for accuracy
       
        img = photo
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
                
        
        output_path = './export/{}_faceD.jpg'
        output_path = output_path.format(filename)
        
        img.save(output_path) 
        return output_path
