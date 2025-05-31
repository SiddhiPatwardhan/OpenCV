import cv2
print("Package imported")

# Chap_1 - Read Images , Videos , Webcam
# To read images we have function imread 
# To display images we use imshow
# We need to add delay inorder to see image for that we use waitKey
# 0 --> infinite delay and 1, 2, 3 --> that many milisecond of delay

img = cv2.imread("Resources/lena.png")
cv2.imshow("Output", img)
cv2.waitKey(0)
