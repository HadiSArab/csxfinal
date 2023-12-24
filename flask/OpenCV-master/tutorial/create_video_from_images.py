# import numpy as np
# import skvideo.io
# import cv2

# out_video =  np.empty([5, 148, 264, 3], dtype = np.uint8)
# out_video =  out_video.astype(np.uint8)

# for i in range(410):
#     img = cv2.imread('extracted_images\\frame_'+str(i)+'.jpg')
#     out_video[i] = img

# # Writes the the output image sequences in a video file
# skvideo.io.vwrite("video.mp4", out_video)
  

import cv2
import numpy as np
import glob

frameSize = (264, 148)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, frameSize)

for filename in glob.glob('D:\python\scraper\OpenCV\\tutorial\extracted_images\*.jpg'):
    img = cv2.imread(filename)
    out.write(img)

out.release()