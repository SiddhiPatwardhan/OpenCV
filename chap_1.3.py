import cv2

# Reading webcam
# To read webcam we use videocapture
# Webcam is same as video. Video is a sequence of images so for that we use while loop to capture all and then show results
# Each parameter has certain id throught which we can adjust them
# 3 --> width , 4 ---> height , 10 ---> brightness

cap = cv2.VideoCapture(0)
# define the parameters
cap.set(3, 640) # setting width
cap.set(4, 480) # setting height
cap.set(10, 100) # changing the brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): # add delay and break loop wj=hen we press q key
        break