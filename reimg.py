import glob as gb
import cv2

img_path = gb.glob('/home/crim/PycharmProjects/untitled1/car_logger/*.png')
img_path.sort()

videoWriter = cv2.VideoWriter('0524t2.avi', cv2.VideoWriter_fourcc('X','V','I','D'), 1, (1280,720))

for path in img_path:
    img  = cv2.imread(path) 
    img = cv2.resize(img,(1280,720))
    videoWriter.write(img)

