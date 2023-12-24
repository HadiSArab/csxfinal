import cv2
from flask import Flask, request, redirect, url_for
from flask import render_template

# http://localhost:5000/image_api?name=images.jpeg&edit=blur,graystyle,resize 

app = Flask(__name__)

@app.route('/image_api')
def image_api():
    name = request.args['name']
    name = str(name)
    name= name.split('.')

    edit = request.args['edit']
    edit = str(edit)
    edit = edit.split(',')
    image = cv2.imread('/home/python/PycharmProjects/OpenCV/image editor/'+str(name[0])+'.'+str(name[1]))

    if 'resize' in edit:
        imgResize150 = cv2.resize(image,(150,150))
        imgResize300 = cv2.resize(image,(300,300))
        imgResize1024 = cv2.resize(image,(1024,1024))
        cv2.imwrite('/home/python/PycharmProjects/OpenCV/image editor/images/'+str(name[0])+'150.'+str(name[1]), imgResize150)
        cv2.imwrite('/home/python/PycharmProjects/OpenCV/image editor/images/'+str(name[0])+'300.'+str(name[1]), imgResize300)
        cv2.imwrite('/home/python/PycharmProjects/OpenCV/image editor/images/'+str(name[0])+'1024.'+str(name[1]), imgResize1024)
    
    if 'blur' in edit:
        imgBlur = cv2.blur(image, (10,10))
        cv2.imwrite('/home/python/PycharmProjects/OpenCV/image editor/images/'+str(name[0])+'Blure.'+str(name[1]), imgBlur)
    
    if 'graystyle' in edit:
        imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('/home/python/PycharmProjects/OpenCV/image editor/images/'+str(name[0])+'Gray.'+str(name[1]), imgGray)



    return "done"