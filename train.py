import cv2
import os
import numpy as np
from PIL import Image
 import pickle
BASE DIR =os.path.dirname(os.path.abspath(_file_)
image dir =os.path.join(BASE DIR, "images"")
face cascade = cv2. CascadeClassifter (C:/Users/RAVI TEJA/intern/harcascade_frontalface_alt2.xml)
recognizer= cv2.face.LBPHFaceRecognizer_createl()
current_id=0
Label_ids={}
y_ labels=[]
x train=[]
for root,dirs,files in os.walk (image_dir):
     for file in files:
         if file.endswith("png") or file.endswith("jpg"): 
            path-os.path.join(root,file)
            label=os.path.basename(os.path.dirname(path)).replace(" ","-").lower ()
            If not label in label ids:
               label ids [label]= current_id 
               current_id+=1
            id = label_ids[label]
            #print (Label ids)
            pil_image=Image.open(path).convert ("L"")
            size - (550,558)
            final_image=pil_image.resize(size,Image.ANTIALIAS)
            image array =np.array(final_image, "uint8")
            #print(image_array)
            faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.5, minNeighbors=5) 
            for(x,y,w,h) in faces:
               roi=image_array[y:y+h,x:x+w]
               x_train.append (roi)
               y_labels.append(id_)
    with open ("labels.pickle",'wb') as f:
      pickLe.dump(label_ids, f)
    recognizer.train(x_train,np.array(y_labels))
    recognizer, save ("test2222.yml")