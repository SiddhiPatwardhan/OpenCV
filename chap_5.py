import cv2
import numpy as np

# chap 5 - Wrap Perspective
# for this we use function get perspective transform and wrap perspective
# A perspective transform allows you to change the perspective from which you view a particular portion of an image. 
# For example, if you take a picture of a rectangular object (like a playing card or a page) from an angle, it looks distorted. 
# With perspective transformation, you can “warp” the image so it appears as if taken from the front (top-down view).
img = cv2.imread("Resources/cards.jpg")

width , height = 250,350
# define 4 corner points of card
pts1 = np.float32([[111, 219],[287, 188],[154, 482],[352, 440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)