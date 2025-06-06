import cv2
import numpy as np

# chap 4 - Shapes and Text

img = np.zeros((512, 512, 3) , np.uint8) # gray scale image
print(img) # check img dimensions

# coloring the whole image
img[:] = 255,0,0

# for creating lines we have cv2,lines function
# starting and ending point of line , colour , thinkness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5) # center point and radius
cv2.putText(img,"OpenCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("Image" , img)
cv2.waitKey(0)