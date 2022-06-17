import cv2
import mediapipe as mp
import time
import os 

cap = cv2.VideoCapture("InputVideo/input.mp4")

while True:
    success, img = cap.read()
    cv2.waitKey(1)
    cv2.imshow("Image",img)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break;
    mpFaceDetection = mp.solutions.face_detection
    faceDetection = mpFaceDetection.FaceDetection()
    mpDraw = mp.solutions.drawing_utils
