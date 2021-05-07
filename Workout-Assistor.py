import cv2
import PoseEstimation
import numpy as np
import time

cap = cv2.VideoCapture(0)
detector = PoseEstimation.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        angle1 = detector.findAngle(img, 11, 13, 15)
        angle2 = detector.findAngle(img, 12, 14, 16)

        percentage1 = np.interp(angle1, (25, 175), (0, 100))
        percentage2 = np.interp(angle2, (25, 175), (0, 100))

        print(angle1, percentage1)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
