import numpy as np
import cv2
face=cv2.CascadeClassifier(r'C:\Users\user\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier(r'C:\Users\user\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_eye.xml')
i=cv2.imread(r'C:\Users\user\Pictures\Google+ Auto Backup\baby.jpg')
gr=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
faces=face.detectMultiScale(gr, 1.3, 5)
for (x,y,w,h) in faces:
     cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)
     gray = gr[y:y+h, x:x+w]
     color = i[y:y+h, x:x+w]
     eyes = eye.detectMultiScale(gray)
     for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',i)
cv2.destroyAllWindows()
