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
class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system") 

        title_lbl=Label(self.root,text="Help Desk" ,font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        top_image=Image.open(r"collage_images\he.jpg")
        top_image=top_image.resize((1530,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(top_image)

        top_img=Label(self.root,image=self.photoimg)
        top_img.place(x=0,y=50,width=1530,height=720)
    
        #help info
        dev_label=Label(top_img,text="Email:purnaalemagar601@gmail.com",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=540,y=550)

       






if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()