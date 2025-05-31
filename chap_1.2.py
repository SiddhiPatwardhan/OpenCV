import cv2

# Reading videos
# To read video we use videocapture
# video is a sequence of images so for that we use while loop to capture all and then show results

cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): # add delay and break loop wj=hen we press q key
        break