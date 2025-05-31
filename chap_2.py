import cv2
import numpy as np

# chap 2 - Basic Functions

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)

# BF1 - Convering image into Gray Scale for this we use cvtColor
# cvtColor = converts your images into different colour scale

# BF2 - Blur image for this will use Gaussian Blur function to blur the image
# k --> kernel size it need to be odd number 3 x 3 or 7 x 7 or 5 x 7

# BF3 - edge detector to find edges of our images for this we will use Canny function
# add threshold functions - to define how much edges do you need - its bassically like a sketch of you image

# Sometimes we are detection an edge but bcoz there is a gap or join properly it doesnt detect it as a proper line
# BF4 - So for that we can increase the thickness of our edge for that we use Dilation function
# The kernel defines the shape and size of the spread.

# BF5 - Opposite to dilation making edges thinner for that we use erode function

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7) , 0)
imgCanny = cv2.Canny(img, 150 , 200)
imgDilation = cv2.dilate(imgCanny , kernel, iterations=1 )
imgEroded = cv2.erode(imgDilation , kernel, iterations=1)


cv2.imshow("Gray Image" , imgGray)
cv2.imshow("Blur Image" , imgBlur)
cv2.imshow("Canny Image" , imgCanny)
cv2.imshow("Dilation Image" , imgDilation)
cv2.imshow("Eroded Image" , imgEroded)
cv2.waitKey(0)