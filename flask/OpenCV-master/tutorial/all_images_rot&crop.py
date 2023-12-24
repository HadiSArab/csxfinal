import cv2
import glob

for filename in glob.glob('D:\ehsaniran\source\*.jpg'):
    img = cv2.imread(filename)

    # extract image name from url
    n = filename.split("\\")
    na = str(n[-1])
    nam = na.split('.')
    name = str(nam[0])

    y,x,ht = img.shape   
    xcrop = int(x/2)
    ycrop = int(y/2)
    matrix180 = cv2.getRotationMatrix2D((x/2,y/2),180,1)
    rot180 = cv2.warpAffine(img,matrix180,(x,y))

    matrix90 = cv2.getRotationMatrix2D((x/2,y/2),90,1)
    rot90 = cv2.warpAffine(img,matrix90,(y,x))

    imgCropped = img[0:ycrop,0:xcrop]
    
    cv2.imwrite("D:\ehsaniran\\rot90\\"+name+"-rot90.jpg",rot90)
    cv2.imwrite("D:\ehsaniran\\rot180\\"+name+"-rot180.jpg",rot180)
    cv2.imwrite("D:\ehsaniran\cropped\\"+name+"-cropped.jpg",imgCropped)
