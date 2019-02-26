import numpy as np
import cv2
#instansiating a cemra object to captutre images
cam = cv2.VideoCapture(0)
#create a haar cascade object for face detection
face_cas=cv2.CascadeClassifier('C:\python3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
#create a placeholder for storing the data
data=[]
i=0;#current frame no
while True:
    ret,frame=cam.read()
    # if the cemra is working fine we procede to extract the face
    if ret==True:
        #convert the current frame to gray scale
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #apply the harr cascade to detect faces in the current frame
        faces=face_cas.detectMultiScale(gray, 1.3, 5)
        #for each face object we get we have
        #the corner coords(x,y)
        #and width and heigt of the face
        for (x,y,w,h) in faces:
            #geting frame component from the image frame
            face_component=frame[y:y+h,x:x+w, :]
            #resizing
            fc=cv2.resize(face_component,(50,50))
            #storing the face data after every 10 frames only if no is less he 20
            if i%10==0 and len(data)<20:
                data.append(fc)
                #for visualization drawing a rectangle around the face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        i+=1
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==27 or len(data)>=20:
            break
    else:
        print("error")
cv2.destroyAllWindows()
data=np.asarray(data)
print(data.shape)
np.save('face_03',data)












