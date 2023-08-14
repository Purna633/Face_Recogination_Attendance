from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x690+0+0")
        self.root.title("face recogination system")
        #variable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

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

        #current courses
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Courses imformation",font=("timesnew romans" ,12,"bold"))
        current_frame.place(x=15,y=10,width=620,height=120)
        #department
        dep_lbl=Label(current_frame,text="Department",font=("timesnew romans" ,12,"bold"),bg="white")
        dep_lbl.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("timesnew romans" ,12,"bold"),width=17,state="read only")
        dep_combo['values']=("Select Department","Accounting ","markting","IT","BCA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         #course
        course_lbl=Label(current_frame,text="Course",font=("timesnew romans" ,12,"bold"),bg="white")
        course_lbl.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("timesnew romans" ,12,"bold"),width=17,state="read only")
        course_combo['values']=("Select Course","BBM","BBS","BBA","BCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_lbl=Label(current_frame,text="Year",font=("timesnew romans" ,12,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("timesnew romans" ,12,"bold"),width=17,state="read only")
        year_combo['values']=("Select Year","2020 ","2021","2022","2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        sem_lbl=Label(current_frame,text="Semester",font=("timesnew romans" ,12,"bold"),bg="white")
        sem_lbl.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("timesnew romans" ,12,"bold"),width=17,state="read only")
        sem_combo['values']=("Select Semester","1 ","2","3","4")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)#semester
        sem_lbl=Label(current_frame,text="Semester",font=("timesnew romans" ,12,"bold"),bg="white")
        sem_lbl.grid(row=1,column=2,padx=10,sticky=W)

        

        #class Student Information
        student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student  imformation",font=("timesnew romans" ,12,"bold"))
        student_frame.place(x=15,y=130,width=620,height=330)

        #student id
        stdid_lbl=Label(student_frame,text="Student ID",font=("timesnew romans" ,12,"bold"),bg="white")
        stdid_lbl.grid(row=0,column=1,padx=10,sticky=W)

        StudentID_entry=ttk.Entry(student_frame,textvariable=self.var_std_id,font=("timesnew romans" ,12,"bold"),width=19,state="read only")
        StudentID_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        #student name
        stdname_lbl=Label(student_frame,text="Name",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        stdname_lbl.grid(row=0,column=3,padx=10,sticky=W)

        Studentname_entry=ttk.Entry(student_frame,textvariable=self.var_std_name,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        Studentname_entry.grid(row=0,column=4,padx=10,pady=10,sticky=W)

        #student division
        stddivision_lbl=Label(student_frame,text="Division",font=("timesnew romans" ,12,"bold"),bg="white")
        stddivision_lbl.grid(row=1,column=1,padx=10,sticky=W)
        div_combo=ttk.Combobox(student_frame,textvariable=self.var_div,font=("timesnew romans" ,12,"bold"),width=17,state="read only")
        div_combo['values']=("A+ ","A","B+","B","C+","C","D+","D","Fail")
        div_combo.current(0)
        div_combo.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        
        #student ROLLNO
        stdroll_lbl=Label(student_frame,text="Roll No",font=("timesnew romans" ,12,"bold"),bg="white")
        stdroll_lbl.grid(row=1,column=3,padx=10,sticky=W)

        Studentdivision_entry=ttk.Entry(student_frame,textvariable=self.var_roll,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        Studentdivision_entry.grid(row=1,column=4,padx=10,pady=10,sticky=W)

        #student Gender
        stddivision_lbl=Label(student_frame,text="Gender",font=("timesnew romans" ,12,"bold"),bg="white")
        stddivision_lbl.grid(row=2,column=1,padx=10,sticky=W)

        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gender,font=("timesnew romans" ,12,"bold"),width=17,state="read only")
        gender_combo['values']=("male ","female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        
        #student Dob
        stddob_lbl=Label(student_frame,text="DOB",font=("timesnew romans" ,12,"bold"),bg="white")
        stddob_lbl.grid(row=2,column=3,padx=10,sticky=W)

        Studentdob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        Studentdob_entry.grid(row=2,column=4,padx=10,pady=10,sticky=W)

        #student email
        stdemail_lbl=Label(student_frame,text="Email",font=("timesnew romans" ,12,"bold"),bg="white")
        stdemail_lbl.grid(row=3,column=1,padx=10,sticky=W)

        Studentemail_entry=ttk.Entry(student_frame,textvariable=self.var_email,font=("timesnew romans" ,12,"bold"),width=19,state="read only")
        Studentemail_entry.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        #student phone
        stdphone_lbl=Label(student_frame,text="Phone",font=("timesnew romans" ,12,"bold"),bg="white")
        stdphone_lbl.grid(row=3,column=3,padx=10,sticky=W)

        Studentphone_entry=ttk.Entry(student_frame,textvariable=self.var_phone,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        Studentphone_entry.grid(row=3,column=4,padx=10,pady=10,sticky=W)

        #student address
        stdaddress_lbl=Label(student_frame,text="Address",font=("timesnew romans" ,12,"bold"),bg="white")
        stdaddress_lbl.grid(row=4,column=1,padx=10,sticky=W)

        Stdaddress_entry=ttk.Entry(student_frame,textvariable=self.var_address,font=("timesnew romans" ,12,"bold"),width=19,state="read only")
        Stdaddress_entry.grid(row=4,column=2,padx=10,pady=10,sticky=W)
        #teacher name
        teach_lbl=Label(student_frame,text="Teacher",font=("timesnew romans" ,12,"bold"),bg="white")
        teach_lbl.grid(row=4,column=3,padx=10,sticky=W)

        teach_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        teach_entry.grid(row=4,column=4,padx=10,pady=10,sticky=W)

        #radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_frame,text="take photo sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=1)
        
        radiobtn2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=5,column=2)

        #button
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=700,height=70)
        #save button
        save_btn=Button(btn_frame,text="save",command=self.add_data,width=15,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=1)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=15,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=2)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=15,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0, column=3)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=15,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=4)

        student_frame1=Frame(left_frame,bg="white",relief=RIDGE)
        student_frame1.place(x=15,y=440,width=620,height=30)

        take_photo_btn=Button(student_frame1,command=self.generate_dataset,text="take a photo sample",width=30,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0, column=1)

        update_photo_btn=Button(student_frame1,text="update photo",width=30,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0, column=2)


        
        #right  lable frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("timesnew romans" ,12,"bold"))
        right_frame.place(x=680,y=10,width=650,height=550)

        img5=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\a.jpg")
        img5=img5.resize((350,140),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(right_frame,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=160)

        img6=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\a.jpg")
        img6=img6.resize((350,140),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        f_lbl=Label(right_frame,image=self.photoimg)
        f_lbl.place(x=350,y=0,width=350,height=160)

        #search system
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12) )
        Search_frame.place(x=5,y=160,width=720,height=60)

        search_lbl=Label(Search_frame,text="Search By",font=("timesnew romans" ,10,"bold"),bg="red",fg="white")
        search_lbl.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("timesnew romans" ,10,"bold"),width=15,state="read only")
        search_combo['values']=("Select Search","Roll_No ","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        search_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("timesnew romans" ,10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0, column=4,padx=5)

        showall_btn=Button(Search_frame,text="Show All",width=12,font=("timesnew romans" ,10,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0, column=5,padx=5)
        
        #TAble frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=225,width=635,height=240)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudetntId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll NO")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotosampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
       

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_Cursor)
        self.fetch_data()

    #function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                messagebox.showinfo("Success","welcome to our collage")
                conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_id.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get()

            
                ))
                conn.commit()
                self. fetch_data()
                conn.charset()
                messagebox.showinfo("Success","student details has bee added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_Cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        

    #update 
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample =%s where Student_ID=%s",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),                                        
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()

                       ))
                else:
                    if not Update:
                          return
                messagebox.showinfo("success","student information updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","student id must be required", parent=self.root)    
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Doyou want delete this student??",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","deleted successfully",parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}",parent=self.root)


    #reset
    def reset_data(self):
        self.var_dep.set("Select Deparment"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #generate data set to take a photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%swhere Student_ID=%s",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),                                        
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()==id+1

                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load predefined data  on face frontal from opencv2
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaleing factor=1.3
                    #menium neighbour =5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","generation the data set")
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}",parent=self.root)   


             



if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()       