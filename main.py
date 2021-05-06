import cv2
import numpy as np

print("imported")

faceCascade = cv2.CascadeClassifier
img = cv2.imread("wallpaperflare.com_wallpaper.jpg")

# kernel = np.ones((5, 5), np.uint8)
#
# imggrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggrey, (7, 7), 0)
# imgcanny = cv2.Canny(img, 100, 100)
# imgdialation = cv2.dilate(imgcanny, kernel, 5)
# imgeroded = cv2.erode(imgdialation, kernel, 5)
#
# # cv2.imshow("imggrey",imggrey)
#
# imgresize = cv2.resize(img,(400,400))
#
# imgcropped = img[0:250,200:500]
cv2.imshow("blur", imgcropped)
cv2.waitKey(0)
# cap =  cv2.VideoCapture(0)
#
# while True:
#     success , img = cap.read()
#     cv2.imshow("vid", img)
#     if cv2.waitKey(1) & 0xFF == ord('q') :
#         break
#
