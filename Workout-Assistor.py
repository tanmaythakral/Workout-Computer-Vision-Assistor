import cv2
import PoseEstimation
import numpy as np
import time

cap = cv2.VideoCapture(0)
detector = PoseEstimation.poseDetector()
dir = 0
count1 = 0
count2 = 0
previousper1 = 0
previousper2 = 0

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        angle1 = detector.findAngle(img, 11, 13, 15)
        angle2 = detector.findAngle(img, 12, 14, 16)

        percentage1 = np.interp(angle1, (25, 175), (0, 100))
        percentage2 = np.interp(angle2, (25, 175), (0, 100))

        if percentage1 == 100.0 and previousper1 == 0:
            count1 +=.5
            previousper1 = 1
        elif percentage1 == 0.0 and previousper1 == 1:
            count1 += .5
            previousper1 = 0

        if percentage2 == 100.0 and previousper2 == 0:
            count2 +=.5
            previousper2 = 1
        elif percentage2 == 0.0 and previousper2 == 1:
            count2 += .5
            previousper2 = 0

        cv2.putText(img, "Right Arm " + str(count1), (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(img, "Left Arm " + str(count2), (50, 130), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)




        print(angle1, percentage1)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
