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
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system") 

        # variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_total=StringVar()


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

        img3=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\t.JPG")
        img3=img3.resize((350,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=350,height=150)

        #background image
        img4=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\d.jpg")
        img4=img4.resize((1530,690),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=140,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendance Management System " ,font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left  lable frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("timesnew romans" ,12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=580)

        #attendence information
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Attendence imformation",font=("timesnew romans" ,12,"bold"))
        current_frame.place(x=15,y=10,width=620,height=450)
         
        #attendence
        attdid_lbl=Label(current_frame,text="AttdID",font=("timesnew romans" ,12,"bold"),bg="white")
        attdid_lbl.grid(row=0,column=1,padx=10,sticky=W)

        AttendenceID_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,textvariable=self.var_atten_id,state="read only")
        AttendenceID_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        #rollnbr
        roll_lbl=Label(current_frame,text="Roll No",font=("timesnew romans" ,12,"bold"),bg="white")
        roll_lbl.grid(row=0,column=3,padx=10,sticky=W)

        Rollno_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,textvariable=self.var_atten_roll,state="read only")
        Rollno_entry.grid(row=0,column=4,padx=10,pady=10,sticky=W)

        #student name
        stdname_lbl=Label(current_frame,text="Name",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        stdname_lbl.grid(row=1,column=1,padx=10,sticky=W)

        Studentname_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,textvariable=self.var_atten_name,state="read only")
        Studentname_entry.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        #department
        dep_lbl=Label(current_frame,text="Department",font=("timesnew romans" ,12,"bold"),bg="white")
        dep_lbl.grid(row=1,column=3,padx=10,sticky=W)

        dep_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,textvariable=self.var_atten_dep,state="read only")
        dep_entry.grid(row=1,column=4,padx=10,pady=10,sticky=W)

        #time
        time_lbl=Label(current_frame,text="Time",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        time_lbl.grid(row=2,column=1,padx=10,sticky=W)

        time_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,textvariable=self.var_atten_time,state="read only")
        time_entry.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        #date
        date_lbl=Label(current_frame,text="Date",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        date_lbl.grid(row=2,column=3,padx=10,sticky=W)

        date_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,textvariable=self.var_atten_date,state="read only")
        date_entry.grid(row=2,column=4,padx=10,pady=10,sticky=W)

        #Attensence Status
        status_lbl=Label(current_frame,text="Status",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        status_lbl.grid(row=3,column=1,padx=10,sticky=W)

        status_combo=ttk.Combobox(current_frame,font=("timesnew romans" ,12,"bold"),width=17,textvariable=self.var_atten_attendance,state="read only")
        status_combo['values']=("Present ","absent")
        status_combo.current(0)
        status_combo.grid(row=3,column=2,padx=2,pady=10,sticky=W)

        #total Attendance
        totalattnd_lbl=Label(current_frame,text="Total Attand",font=("timesnew romans" ,12,"bold"),bg="white",width=10)
        totalattnd_lbl.grid(row=3,column=3,padx=10,sticky=W)

        total_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,textvariable=self.var_total,state="read only")
        total_entry.grid(row=3,column=4,padx=10,pady=10,sticky=W)

        #button
        
        btn_frame=Frame(current_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=270,width=580,height=100)

        #save button
        save_btn=Button(btn_frame,text="import csv",command=self.importCsv,width=13,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=1,padx=4,pady=30,sticky=W)

        update_btn=Button(btn_frame,text="export csv",command=self.exportCsv,width=13,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=2)

        delete_btn=Button(btn_frame,text="update",width=13,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0, column=3)

        reset_btn=Button(btn_frame,text="reset",width=13,command=self.reset_data,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=4)

        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attandence",font=("timesnew romans" ,12,"bold"))
        right_frame.place(x=680,y=10,width=650,height=550)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=6,y=6,width=635,height=450)


        #table scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendence","total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")

        self.AttendenceReportTable.pack(fill=BOTH, expand=1)
        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence Status")
        self.AttendenceReportTable.heading("total",text="TotalAttendence")

        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)
        self.AttendenceReportTable.column("total",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        

        #feth data
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"), ("ALl File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("no data","no data found to be export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"), ("ALl File","*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exporte","your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        self.var_total.set(rows[7])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_total.set("")

        
            
        







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()