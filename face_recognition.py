from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognination:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system") 
 
        title_lbl=Label(self.root,text="FACE REOGNITATION" ,font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # 1st image
        top_image=Image.open(r"collage_images\f.jpg")
        top_image=top_image.resize((650,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(top_image)

        top_img=Label(self.root,image=self.photoimg)
        top_img.place(x=0,y=55,width=650,height=680)


        #second image
        bottom_image=Image.open(r"collage_images\f2.png")
        bottom_image=bottom_image.resize((950,680),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(bottom_image)

        bottom_img=Label(self.root,image=self.photoimg1)
        bottom_img.place(x=650,y=55,width=950,height=680)

        #button
        b1=Button(bottom_img,command=self.face_recog,text="Face Recognitation",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1.place(x=365,y=600,width=200,height=40)

    def mark_attendance(self,i,r,n,d,t1):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                Entry=line.split(",")
                name_list.append(Entry[0])

            if((i not in name_list) and (r not in name_list)and (n not in name_list)and (d not in name_list)and (t1 not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present,{t1}")

        


    #face recognitation
    def face_recog(self):
        
        def draw_boundry(img,classlifier,scaleFactor,minNeighbors,color,text,clf):
             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
             features=classlifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
             coord=[]
            

             for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100* (1 - predict / 300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT Student_ID FROM student WHERE Student_ID=" +str(id))
                i=my_cursor.fetchone()
                i="+".join(i)if i is not None else "Unknown"


                my_cursor.execute("SELECT Name FROM student WHERE Student_ID=" +str(id))
                n=my_cursor.fetchone()
                n="+".join(n)if n is not None else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)if r is not None else "Unknown"

                
                my_cursor.execute("SELECT Dep FROM student WHERE Student_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)if d is not None else "Unknown"

                my_cursor.execute("SELECT Total FROM student WHERE Student_ID="+str(id))
                t1=my_cursor.fetchone()
                t1="+".join(t1)if t1 is not None else "Unknown"
               


                if confidence>77:
                    cv2.putText(img,f"stdid:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"dep:{d}",(x,y -5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    #cv2.putText(img,f"Total:{t1}",(x,y -90),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d,t1)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unkonwn Face",(x,y+5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
             return coord
              
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            #coord = draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
    
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face rocognitation",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognination(root)
    root.mainloop()