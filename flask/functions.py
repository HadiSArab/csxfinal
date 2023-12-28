from rembg import remove
from PIL import Image
import cv2
import numpy as np
import mediapipe as mp




def rmbg(photo,filename):
    output_path = './static/export/{}_rmbg.png'
    output_path = output_path.format(filename)

    input = Image.open(photo)
    output = remove(input)
    
    output.save(output_path) 
    return output_path

# ................................................................angle ask from user
def rot(filename):
    angle=90
    photo = cv2.imread("static/uploads/" + filename)
    y,x,ht= photo.shape
    matrix= cv2.getRotationMatrix2D((x/2,y/2),angle,1)
    output = cv2.warpAffine(photo, matrix, (x,y))
    
    fname = filename.split(".")[0]
    output_path = './static/export/{}_rot90.jpg'
    output_path = output_path.format(fname)
    
    cv2.imwrite(output_path, output) 
    return output_path


def Gray(filename):
    
    photo = cv2.imread("static/uploads/" + filename)
    
    output = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    fname = filename.split(".")[0]
    output_path = './static/export/{}_gray.jpg'
    output_path = output_path.format(fname)
    
    cv2.imwrite(output_path, output) 
    return output_path

def Blur(filename):
    
    photo = cv2.imread("static/uploads/" + filename)
    
    output = cv2.blur(photo,(50,5))

    fname = filename.split(".")[0]
    output_path = './static/export/{}_Blur.jpg'
    output_path = output_path.format(fname)
    
    cv2.imwrite(output_path, output) 
    return output_path

def Canny(filename):
    
    photo = cv2.imread("static/uploads/" + filename)
    
    output = cv2.Canny(photo,200,200)

    fname = filename.split(".")[0]
    output_path = './static/export/{}_Canny.jpg'
    output_path = output_path.format(fname)
    
    cv2.imwrite(output_path, output) 
    return output_path



def find_face(filename):

    
    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection(0.5)                            # by default (0.5) and you can change it for accuracy
    
    image_path = 'static/uploads/' + filename
    img = cv2.imread(image_path)
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
            cv2.rectangle(img, bbox , (0,0,255),4)
            cv2.putText(img, f'{int(detection.score[0] * 100)} %', (int(bboxC.xmin * iw),int ((bboxC.ymin * ih)- 20)), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,0), 1)
            
    fname = filename.split(".")[0]
    output_path = './static/export/{}_faceD.jpg'
    output_path = output_path.format(fname)
    cv2.imwrite(output_path, img)
    # img.save() 
    return output_path
