from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
import numpy as np
import cv2
import os
import random
from datetime import datetime
from amcat_enhance_login.forms import registration_form
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
          
def main(request):
    

            
    #return render(request,'index.html')
    return render(request,'home.html')

def login_func(request):
    ''' Function to take user information '''
    form=registration_form()
    if request.method=='POST':
        form=registration_form(request.POST,request.FILES)
        if form.is_valid():
            PIC_DATABASE_DIR=os.path.join(BASE_DIR,'media')
            print(PIC_DATABASE_DIR)
            #STATIC_DIR=os.path.join(BASE_DIR,'static')

            #If form was valid grap photo
            #instansiating a cemra object to captutre images
            cam = cv2.VideoCapture(0)
            classify_path=os.path.join(BASE_DIR ,'classifier\haarcascade_frontalface_default.xml')
            #create a haar cascade object for face detection
            face_cas=cv2.CascadeClassifier(classify_path)
            #create a placeholder for storing the data
            data=[]
            i=0;#current frame no
            user_name="Sitanshu"
            camera = cv2.VideoCapture(0)
            k=0
            hash_code=random.randint(10,10000000)
            dirname=datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45
            t=os.mkdir(os.path.join(PIC_DATABASE_DIR,'image_database', user_name+dirname+str(hash_code)))
            print(t)
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
                            cv2.imwrite(os.path.join(PIC_DATABASE_DIR,'image_database', user_name+dirname+str(hash_code),user_name+str(k)+'.png'),fc)
                            k=k+1
                        #for visualization drawing a rectangle around the face
                    #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    i+=1
                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1)==27 or len(data)>=20:
                        break
                else:
                    print("error")
            cv2.destroyAllWindows()
            data=np.asarray(data)
            #print(data.shape)
            #np.save('face_03',data)"""
            form.save()
            return render(request, 'login_app/success.html')
    return render(request, 'login_app/form_upload.html', {
        'form': form
    })

