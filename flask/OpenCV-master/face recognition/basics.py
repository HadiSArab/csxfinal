import cv2
import face_recognition

ehsan = face_recognition.load_image_file('/home/python/PycharmProjects/OpenCV/tutorial/face data set/alikhani1.jpeg')
ehsan = cv2.cvtColor(ehsan,cv2.COLOR_BGR2RGB)
amin = face_recognition.load_image_file('/home/python/PycharmProjects/OpenCV/tutorial/face data set/amin1.jpg')
amin = cv2.cvtColor(amin,cv2.COLOR_BGR2RGB)
roya = face_recognition.load_image_file('/home/python/PycharmProjects/OpenCV/tutorial/face data set/roya1.jpg')
roya = cv2.cvtColor(roya,cv2.COLOR_BGR2RGB)
Test = face_recognition.load_image_file('/home/python/PycharmProjects/OpenCV/tutorial/face data set/asrjadid.jpg')
Test = cv2.cvtColor(Test,cv2.COLOR_BGR2RGB)
 
faceLocehsan= face_recognition.face_locations(ehsan)[0]
encodeehsan = face_recognition.face_encodings(ehsan)[0]
cv2.rectangle(ehsan,(faceLocehsan[3],faceLocehsan[0]),(faceLocehsan[1],faceLocehsan[2]),(255,0,255),2)
 
faceLocamin= face_recognition.face_locations(amin)[0]
encodeamin = face_recognition.face_encodings(amin)[0]
cv2.rectangle(amin,(faceLocamin[3],faceLocamin[0]),(faceLocamin[1],faceLocamin[2]),(255,0,255),2)

faceLocroya= face_recognition.face_locations(roya)[0]
encoderoya = face_recognition.face_encodings(roya)[0]
cv2.rectangle(roya,(faceLocroya[3],faceLocroya[0]),(faceLocroya[1],faceLocroya[2]),(255,0,255),2)

faceLocTest= face_recognition.face_locations(Test)[0]
encodeTest = face_recognition.face_encodings(Test)[0]
cv2.rectangle(Test,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeehsan,encodeamin,encoderoya],encodeTest)
faceDis = face_recognition.face_distance([encodeehsan,encodeamin,encoderoya],encodeTest)
print(results,faceDis)
cv2.putText(ehsan,f'{results[0]} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.putText(amin,f'{results[1]} {round(faceDis[1],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.putText(roya,f'{results[2]} {round(faceDis[2],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
cv2.imshow('ehsan',ehsan)
cv2.imshow('amin',amin)
cv2.imshow('roya',roya)
cv2.imshow('test',Test)
cv2.waitKey(0)
