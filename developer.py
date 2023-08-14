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
import csv
from tkinter import filedialog

mydata=[]
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system") 

        title_lbl=Label(self.root,text="Developer" ,font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        top_image=Image.open(r"collage_images\de.jpg")
        top_image=top_image.resize((1530,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(top_image)

        top_img=Label(self.root,image=self.photoimg)
        top_img.place(x=0,y=50,width=1530,height=720)
        
        #frame
        main_frame=Frame( top_img,bd=2,bg="white")
        main_frame.place(x=850,y=10,width=500,height=600)

        top_image1=Image.open(r"collage_images\p.jpg")
        top_image1=top_image1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(top_image1)

        top_img1=Label(main_frame,image=self.photoimg1)
        top_img1.place(x=330,y=0,width=160,height=200)

        #developer info
        dev_label=Label(main_frame,text="Hello, my name is  Purna Aale.",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text=" I am fullstack Developer.",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        top_image2=Image.open(r"collage_images\b.jpg")
        top_image2=top_image2.resize((500,480),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(top_image2)

        top_img2=Label(main_frame,image=self.photoimg2)
        top_img2.place(x=0,y=200,width=500,height=500)






if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()