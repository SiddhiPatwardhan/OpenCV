import cv2
import numpy as np
# chap 3 - Resizing and Cropping
# positive x axis --> east
# positive y axis --> south
# for resizing will use resize function
# for cropping we just use slicing

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(300, 200))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image", img)
cv2.imshow("ResizeImage", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)