from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# Create your views here.
import numpy as np
import cv2
import os
import random
from datetime import datetime
from amcat_enhance_login.forms import registration_form
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
global_lables=[]
PIC_DATABASE_DIR=os.path.join(BASE_DIR,'media')
            
user_name_first_name=""
user_name_last_name=""
def main(request):
    

            
    #return render(request,'index.html')
    return render(request,'home.html')

def login_func(request):
    ''' Function to take user information '''
    form=registration_form()
    if request.method=='POST':
        form=registration_form(request.POST,request.FILES)
        if form.is_valid():
            #first_name
            print(PIC_DATABASE_DIR)
            #STATIC_DIR=os.path.join(BASE_DIR,'static')
            user_name_first_name=form.cleaned_data['first_name']
            user_name_last_name=form.cleaned_data['last_name']
            
            #If form was valid grap photo

            #print(form[first_name]) 
            #instansiating a cemra object to captutre images\

            cam = cv2.VideoCapture(0)
            classify_path=os.path.join(BASE_DIR ,'classifier\haarcascade_frontalface_default.xml')
            #create a haar cascade object for face detection
            face_cas=cv2.CascadeClassifier(classify_path)
            #create a placeholder for storing the data
            data=[]
            i=0;#current frame no
            camera = cv2.VideoCapture(0)
            k=0
            hash_code=random.randint(10,10000000)
            dirname=datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45
            t=os.mkdir(os.path.join(PIC_DATABASE_DIR,'image_database', user_name_first_name+user_name_last_name+dirname+str(hash_code)))
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
                            cv2.imwrite(os.path.join(PIC_DATABASE_DIR,'image_database', user_name_first_name+user_name_last_name+dirname+str(hash_code),str(k)+'.png'),fc)
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
            global_lables.append(user_name_first_name+user_name_last_name)
            np.save(os.path.join(PIC_DATABASE_DIR,'image_numpy_py',user_name_first_name+user_name_last_name),data)
            form.save()
            return render(request, 'login_app/success.html')
    return render(request, 'login_app/form_upload.html', {
        'form': form
    })


def knn_start(request):
    cam = cv2.VideoCapture(0)
    face_cas=os.path.join(BASE_DIR ,'classifier\haarcascade_frontalface_default.xml')
    #declare the type of font to be used on output window
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #load the data from the numpy matrices and convert to linear vectors
    f_01=np.load(os.path.join(PIC_DATABASE_DIR,'image_numpy_py'),user_name_first_name+user_name_last_name+".npy").reshape((-1, 50*50*3))	# Shubham
    #f_02 = np.load('face_02.npy').reshape((-1, 50*50*3))	# vivek
    #f_03 = np.load('face_03.npy').reshape((-1, 50*50*3))	# parth
    #create a look-up dictionary
    """
    names = {
	0: 'Shubham',
	1: 'vivek', 
	2: 'shobhit',}"""
    # create a matrix to store the labels
    labels = np.zeros((1000000, 1))
    start=0
    for i in range(len(global_lables)):
        labels[start:start+20:]
        start=start+20
    
    # combine all info into one data array
    data = np.concatenate([f_01,])	# (60, 7500)
    print (data.shape, labels.shape)	# (60, 1)
    # the distance and knn functions we defined earlier
    def distance(x1, x2):
        return np.sqrt(((x1-x2)**2).sum())
    def knn(x, train, targets, k=5):
        m = train.shape[0]
        dist = []
    for ix in range(m):
        # compute distance from each point and store in dist
        dist.append(distance(x, train[ix]))
        dist = np.asarray(dist)
        indx = np.argsort(dist)
        sorted_labels = labels[indx][:k]
        counts = np.unique(sorted_labels, return_counts=True)
        return counts[0][np.argmax(counts[1])]
    while True:
        # get each frame
        ret, frame = cam.read()
        if ret == True:
            # convert to grayscale and get faces
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cas.detectMultiScale(gray, 1.3, 5)
            # for each face
            for (x, y, w, h) in faces:
                face_component = frame[y:y+h, x:x+w, :]
                fc = cv2.resize(face_component, (50, 50))

			# after processing the image and rescaling
			# convert to linear vector using .flatten()
			# and pass to knn function along with all the data
                lab = knn(fc.flatten(), data, labels)
			# convert this label to int and get the corresponding name
                text = names[int(lab)]
                cv2.putText(frame, text, (x, y), font, 1, (255, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow('face recognition', frame)
            if cv2.waitKey(1) == 27:
                break
        else:
            print ('Error')
    cv2.destroyAllWindows()

    
