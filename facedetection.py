'''
Those libraries are required 
so the code can run properly
u can download them using :
- Windows : pip install "Name of the library"
'''
import cv2 as cv
import numpy as np
import os
import pyautogui as auto
# #---------------------------------------------------------------------------------------------------------------------------------------------------------------

capture= cv.VideoCapture(0, cv.CAP_DSHOW)
    
def ChangeRes(width, height):
    # only live video
    capture.set(3,width)
    capture.set(4,height)
    
def rescaleFrame(frame, scale = 1.0):
    #we are rescaling the img/window
    
    width =int(frame.shape[1]*scale)
    height =int( frame.shape[0]*scale)
    dimensons = (width,height)
    return cv.resize(frame, dimensons, interpolation=cv.INTER_AREA)
while True:
    
    isTrue, frame = capture.read()
    
    haar_cascade = cv.CascadeClassifier(r"*PUT THE PATH OF THE INSTALLED XML FILE")

    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize= (100,100), maxSize=(200,200))
    
    for (x,y,w,h) in faces_rect:
        g = cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        cv.putText(frame, "Face", (x,y), cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,255), 2)
    cv.putText(frame, "press 'd' to exit", (30,30), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)
    cv.putText(frame,"faces detected :"+ str(len(faces_rect)), (300,30), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 2)
    cv.imshow("Face Detection by MX'Softwares", frame)
    
    if cv.waitKey(delay= 100) & 0xFF==ord('d'):
        cv.destroyAllWindows()
        quit()
            

else :
    auto.confirm(title = "face detection", text="ERROR: No camera detected or software error", butttons= ["Ok"])
    time.sleep(4)
    quit()

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
