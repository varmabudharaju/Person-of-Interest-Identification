import numpy as np
import cv2
import pickle
import sys
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def send_mail(frame):
 mail_content = '''check this out'''
 sender_address = 'sairamvarma0010@gmail.com'
 sender_pass = 'varma1215316310'
 receiver_address = 'sairamvarma009@gmail.com.com'
 message = MIMEMultipart()
 message['From'] = sender_address
 message['To'] = receiver_address
 message['Subject'] = 'A test mail sent by Python. It has an attachment.'
 message.attach(MIMEText(mail_content, 'plain'))

 attach_file_name = 'mailtest.png'
 attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
 payload = MIMEBase('application', 'octate-stream')
 payload.set_payload((attach_file).read())
 encoders.encode_base64(payload) #encode the attachment
 payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
 message.attach(payload)
 session = smtplib.SMTP('smtp.gmail.com', 587)
 session.starttls()
 session.login(sender_address, sender_pass)
 text = message.as_string()
 session.sendmail(sender_address, receiver_address, text)
 session.quit()
 print('Mail Sent')
faceCascade = cv2.CascadeClassifier('C:/Users/RAVI TEJA/intern/haarcascade_frontalface_alt2.xml')
eye_cascade=cv2.CascadeClassifier('C:/Users/RAVI TEJA/intern/haarcascade_eye.xml')
recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read("test2222.yml")

labels ={"person_name":1}
with open("labels.pickle",'rb') as f:
   og_labels = pickle.load(f)
   labels ={v:k for k,v in og_labels.items()}

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( gray,scaleFactor=5,minNeighbors=5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
         #print(x,y,w,h)
         
         
         roi_gray=gray[y:y+h,x:x+w]
         roi_color=frame[y:y+h,x:x+w]
         
         
         id_,conf=recognizer.predict(roi_gray)
         if conf>45 and conf<=64:
            # print(id_)
             print(labels[id_])
             print(conf)
             font=cv2.FONT_HERSHEY_SIMPLEX
             name=labels[id_]
             color=(255,255,255)
             stroke=2
             cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
         
         img_item="mailtest200.png"
         cv2.imwrite(img_item,roi_gray)
         color=(255,0,0)
         stroke=2
         end_cord_x=x+w
         end_cord_y=y+h 
         cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y),color,stroke)
         eyes=eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh)in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
send_mail(frame=frame)