from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")

        title_lbl=Label(self.root,text="TRAIN DATASET" ,font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        top_image=Image.open(r"collage_images\t1.jpg")
        top_image=top_image.resize((1530,340),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(top_image)

        top_img=Label(self.root,image=self.photoimg)
        top_img.place(x=0,y=40,width=1530,height=340)

        #button
        b1=Button(self.root,text="TRAIN DATASET",command=self.train_classifier,font=("times new roman",30,"bold"),bg="red",fg="white")
        b1.place(x=0,y=380,width=1530,height=40)

        bottom_image=Image.open(r"collage_images\t2.jpg")
        bottom_image=bottom_image.resize((1530,340),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(bottom_image)

        top_img=Label(self.root,image=self.photoimg1)
        top_img.place(x=0,y=420,width=1530,height=340)

    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray imgae scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)
        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()

        #clf=cv2.face.createLBPHFaceRecognizer()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training dataset ccompleted")

        


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()