from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk
from Student import student
import  os 
from train import Train
from face_recognition import Face_Recognination
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recogination_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")

        img=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\a.jpg")
        img=img.resize((350,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=150)

        img1=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\b.jpg")
        img1=img1.resize((350,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=350,y=0,width=350,height=150)

        img2=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\ref.PNG")
        img2=img2.resize((350,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=690,y=0,width=360,height=150)

        img12=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\t.JPG")
        img12=img12.resize((350,150),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        f_lbl=Label(self.root,image=self.photoimg12)
        f_lbl.place(x=1020,y=0,width=350,height=150)
        

        #background image
        img3=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\d.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=140,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGINATION SYSTEM SOFTWARE " ,font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        def time():
          String =strftime('%H:%M:%S %p')
          lb21.config(text = String)
          lb21.after(1000, time)

        lb21=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lb21.place(x=0,y=0,width=110,height=50)
        time()


        #student details button
        img4=Image.open(r"collage_images\ac.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=60,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=150,y=240,width=220,height=40)

        #Detect face button
        img5=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\t.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(bg_img,command=self.face_deta,image=self.photoimg5,cursor="hand2")
        b5.place(x=420,y=60,width=220,height=220)

        b5_1=Button(bg_img,command=self.face_deta,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b5_1.place(x=420,y=240,width=220,height=40)

        #Attendence button
        img6=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\b.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b6.place(x=720,y=60,width=220,height=220)

        b6_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b6_1.place(x=720,y=240,width=220,height=40)

        #help button
        img7=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\he.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b7.place(x=1000,y=60,width=220,height=220)

        b7_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b7_1.place(x=1000,y=240,width=220,height=40)

        #train button
        img8=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\d.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b8=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b8.place(x=150,y=300,width=220,height=220)

        b8_1=Button(bg_img,command=self.train_data,text="Train",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b8_1.place(x=150,y=500,width=220,height=40)

        #photos  face button
        img9=Image.open(r"collage_images\b.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b9=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b9.place(x=420,y=300,width=220,height=220)

        b9_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b9_1.place(x=420,y=500,width=220,height=40)

        #Developer  button
        img10=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\de.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b10=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b10.place(x=720,y=300,width=220,height=220)

        b10_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b10_1.place(x=720,y=500,width=220,height=40)

        #Exit button
        img11=Image.open(r"collage_images\e.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b11=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.isExit)
        b11.place(x=1000,y=300,width=220,height=220)

        b11_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b11_1.place(x=1000,y=500,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def isExit(self):
        self.isExit = messagebox.askyesno("face Recognition","Are you sure to exit this project",parent=self.root)
        if self.isExit > 0:
          self.root.destroy()
        else:
         return
        
    #function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_deta(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognination(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        

        



             

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recogination_system(root)
    root.mainloop()