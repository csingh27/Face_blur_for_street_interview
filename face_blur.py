import cv2
import mediapipe
import time
import os 

cap = cv2.VideoCapture("InputVideo/input.mp4")

while True:
    success, img = cap.read()
