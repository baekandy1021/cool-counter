import cv2 as cv
import time
import HandTrackingModule as htm

wCam, hCam = 640,480
cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4, hCam)

pTime = 0 
detector = htm.handDetector(detectionCon= 0.75)

tipIds =[4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw= False)

    if len(lmList) != 0:
        fingers = []
        #thumb
        if lmList[4][1] < lmList[2][1]:
            fingers.append(1)
        else: 
            fingers.append(0)
        #4 fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else: 
                fingers.append(0)
        
        print(fingers)
        totalFingers = fingers.count(1)
        cv.putText(img, f'Number: {totalFingers}', (40,140), cv.FONT_HERSHEY_COMPLEX, 1, (200,0,0), 2)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (40,70), cv.FONT_HERSHEY_COMPLEX, 1, (200,0,0), 2)
    cv.imshow("image", img)
    cv.waitKey(5)