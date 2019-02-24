#Import the libraries.
import numpy as np
import cv2
#open the web camera default is 0 to use external web camera use 1.
camera=cv2.VideoCapture(0)
#getting the face casecade object.
face_cas=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
#store the face values in list data
faces_data=[]
#current frame number
ix=0
while True:
    #if camera detect an object it return true and it frams value(numpy matrix)
    ret,frame=camera.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cas.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            face_component=frame[y:y+h,x:x+w,:]
            fc=cv2.resize(face_component,(50,50))
            if ix%10==0 and len(faces_data)<20:
                faces_data.append(fc)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        ix+=1
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==27 or len(faces_data)>=20:
            break
                
    else:
        print("Error")

cv2.destroyAllWindows()
faces_data=np.asarray(faces_data)
print(faces_data.shape)
print(faces_data)

