import cv2
import glob
import keras
from keras.layers import Activation, Conv2D, MaxPooling2D
from tflearn.layers.normalization import local_response_normalization
from sklearn.preprocessing import LabelEncoder

faceDet = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
emotions = ['angry','disgust','sad','fear','surprise','happy','neutral']
features = []



def detect_faces(emotion):
    files = glob.glob("jaffe/%s/*" %(emotion))
    filenumber,i = 0,0
    for f in files:
        gray = cv2.imread(f)
        """gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY) #Convert image to grayscale"""
        face = faceDet.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
        """if len(face) == 1:
            facefeatures = face
        else:
            facefeatures = ""  """
        for (x, y, w, h) in face:
            gray = gray[y:y+h, x:x+w]
            try:
                out = cv2.resize(gray, (224, 224))
                features.append(Alexnet(out))
                cv2.imwrite("dataset/%s/%s.jpg" %(emotion,filenumber), out)
            except:
               pass
        filenumber += 1

for emotion in emotions:
    detect_faces(emotion)



def Alexnet(network):
    network = Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11), strides=(4,4), padding='valid')(network)
    network = Activation('relu')(network)
    network = MaxPooling2D(pool_size=(2,2), kernel_size=(3,3), strides=(2,2), padding='valid')(network)
    network = local_response_normalization(network)
    
    network = Conv2D(filters=256, kernel_size=(5,5), strides=(1,1), padding='valid')(network)
    network = Activation('relu')(network)
    network = MaxPooling2D(pool_size=(2,2), kernel_size=(3,3), strides=(2,2), padding='valid')(network)
    network = local_response_normalization(network)

    network = Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid')(network)
    network = Activation('relu')(network)
    network = Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid')(network)
    network = Activation('relu')(network)

    network = Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid')(network)
    network = Activation('relu')(network)
    network = MaxPooling2D(pool_size=(2,2),kernel_size=(3,3), strides=(2,2), padding='valid')(network)
    
    return (network)


labelencoder = LabelEncoder()
x = labelencoder.fit_transform(emotions)
label_emotion=[*[x[0]]*30,*[x[1]]*29,*[x[2]]*32,*[x[3]]*31,*[x[4]]*30,*[x[5]]*31,*[x[6]]*30]


f = open("face_date.csv", "w")
for i in range(len(features)):
    f.write("{},{}\n".format(features[i], label_emotions[i]))
f.close()
