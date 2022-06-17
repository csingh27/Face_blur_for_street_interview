import cv2
import mediapipe as mp
import time
import os 

cap = cv2.VideoCapture("InputVideo/input.mp4")

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    if success:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(imgRGB)
        if results.detections:
            for id, detection in enumerate(results.detections):
                print(id, detection)
                print(detection.location_data.relative_bounding_box)
                # mpDraw.draw_detection(img, detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                print(bbox)
                cv2.rectangle(img,bbox, (255,0,0),2)
                cv2.putText(img, "Face",
                        (bbox[0],bbox[1] - 20),cv2.FONT_HERSHEY_PLAIN, 3, (255,255,0), 2)
        cv2.waitKey(1)
        cv2.imshow("Image",img)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break;
        
