import cv2
import mediapipe as mp
import time
import os 

cap = cv2.VideoCapture("InputVideo/input.mp4")

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()
mpDraw = mp.solutions.drawing_utils

i = 0
interview_start = 580
interview_end = 8200

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("OutputVideo/output.mp4",fourcc,30.0,(1280,720))

while True:
    success, img = cap.read()
    i = i + 1
    if success:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(imgRGB)
        if results.detections:
            for id, detection in enumerate(results.detections):
                # print(id, detection)
                # print(detection.location_data.relative_bounding_box)
                # mpDraw.draw_detection(img, detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                # print(bbox)
                # cv2.rectangle(img,bbox, (255,0,0),2)
                # cv2.putText(img, "Face",
                #      (bbox[0],bbox[1] - 20),cv2.FONT_HERSHEY_PLAIN, 3, (255,255,0), 2)
        factor = 3.0
        xmin = bbox[0]
        ymin = bbox[1]
        h = bbox[2]
        w = bbox[3]
        face = img[ymin: ymin + h, xmin: xmin + w]
        kW = int(w / factor)
        kH = int(h / factor)
        if kW % 2 == 0:
            kW -= 1
        if kH % 2 == 0:
            kH -= 1
        if(i>interview_start and i<interview_end):
            if(face.any()):
                face = cv2.GaussianBlur(face, (kW,kH), 0)
        img[ymin: ymin + h, xmin: xmin + w] = face
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break;
        cv2.waitKey(1)
        cv2.imshow("Image",img)
        out.write(img)
