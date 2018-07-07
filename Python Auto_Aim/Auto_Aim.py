import numpy as np
import math
import cv2 as cv
from PIL import ImageGrab


face_cascade = cv.CascadeClassifier('C:/Users/joshu/Documents/Learn_Python/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:/Users/joshu/Documents/Learn_Python/venv/Lib/site-packages/cv2/data/haarcascade_eye.xml')



while(True):
    img = ImageGrab.grab(bbox = (0,0,960,1080))
    img_np = np.array(img)
    gray = cv.cvtColor(img_np, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    for (x,y,w,h) in faces:
        cv.rectangle(gray, (x, y), (x + w, y + h), (255,0,0), 2)
        roi_gray = gray[y: y+h, x: x+ w]
    cv.imshow('img', gray)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()