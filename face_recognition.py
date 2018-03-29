#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 18:06:03 2018

@author: abhishek
"""
#inporting the library
import cv2

#locading the cascades
face_cascade = cv2.CascadeClassifier('harrcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('harrcascade_eye.xml')

#Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces: # iterate through the faces to draw the faces
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # detect the eyes , in the face reigons
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) #take the eye_cascade object
        for(ex,ey,ew,eh) in eyes: # iterate through the faces to draw the faces
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
    return frame
        
