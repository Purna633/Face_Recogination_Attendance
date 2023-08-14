from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
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


def main():
     win=Tk()
     app=Login(win)
     win.mainloop()
  
     
     


class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system") 
       
        img3=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\login.jpg")
        img3=img3.resize((1530,920),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=700)

        frame=Frame(self.root,bg="purple")
        frame.place(x=550,y=160,width=340,height=450)

        img=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\admin2.png")
        img=img.resize((100,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        img=Label(image=self.photoimg,bg="purple",borderwidth=0)
        img.place(x=670,y=160,width=100,height=100)

        str_lbl=Label(frame,text="Get Started",font=("timesnew romans" ,12,"bold"),fg="white",bg="purple")
        str_lbl.place(x=120,y=100)

        #label
        username_lbl=Label(frame,text="Username",font=("timesnew romans" ,12,"bold"),fg="white",bg="purple")
        username_lbl.place(x=70,y=140)

        self.txtUser=Entry(frame,font=("timesnew romans" ,12,"bold"))
        self.txtUser.place(x=40,y=170,width=270)

        password_lbl=Label(frame,text="Password",font=("timesnew romans" ,12,"bold"),fg="white",bg="purple")
        password_lbl.place(x=70,y=220)

        self.txtPassword=Entry(frame,font=("timesnew romans" ,12,"bold"))
        self.txtPassword.place(x=40,y=250,width=270)

        #image icon
        img1=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\admin1.png")
        img1=img1.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img1)

        img1=Label(image=self.photoimg2,bg="purple",borderwidth=0)
        img1.place(x=590,y=295,width=25,height=25)

        img2=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\pass.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img2)

        img2=Label(image=self.photoimg4,bg="purple",borderwidth=0)
        img2.place(x=590,y=380,width=25,height=25)


        #login button
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,command=self.login,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password,font=("times new roman",12,"bold"),bd=3,borderwidth=0,fg="white",bg="purple",activeforeground="white",activebackground="red")
        forgetbtn.place(x=40,y=360,width=120,height=35)

        registerbtn=Button(frame,text="Register Now",command=self.register_window,font=("times new roman",12,"bold"),bd=3,borderwidth=0,fg="white",bg="purple",activeforeground="white",activebackground="red")
        registerbtn.place(x=190,y=360,width=120,height=35)


    def register_window(self):
         self.new_window=Toplevel(self.root)
         self.app=Register(self.new_window)

    def login(self):
        if self.txtUser.get()=="" or self.txtPassword.get()=="":
            messagebox.showerror("Error","all field are required")

        elif self.txtUser.get()=="purna" and self.txtPassword.get()=="ale":
            messagebox.showinfo("successfull","welcome to face recogination attendence system")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register1 where email=%s and password=%s",(
                                        self.txtUser.get(),
                                        self.txtPassword.get()

            ))
            row=my_cursor.fetchone()
            if row==None:
                 messagebox.showerror("Error","invalid username and password")

            else:
                 open_main=messagebox.askyesno("yeesNo","Access only admin")
                 if open_main>0:
                      self.new_window=Toplevel(self.root)
                      self.app=Face_Recogination_system(self.new_window)

                 else:
                     if not open_main:
                         return 
                     
            conn.commit()
            conn.close()


    def reset_password(self):
        if self.txtcontact.get()=="Select":
            messagebox.showerror("Error","enter your mobile nbr")

        elif self.txtlpass.get()=="":
            messagebox.showerror("Error","please enter the new password")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
            my_cursor=conn.cursor()
            query=("select * from register1 where email=%s and contact=%s")
            value=(self.txtcontact.get(),self.txtlpass.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","please enter correct contact nbr")

            else:
                query=("update register1 set password=%s where email=%s")
                value=(self.txtlpass.get(),self.txtcontact.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your password has been reset , please login with  new password")



    def forgot_password(self):
        if self.txtUser.get()=="":
            messagebox.showerror("Error","please enter  the email to reset password")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
            my_cursor=conn.cursor()
            query=("select * from register1 where email= %s")
            value=(self.txtUser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("my error","please enter the valid email")

            else:
                conn.close()
                self.root2=Toplevel()
                self.root.title("Forger Password")
                self.root2.geometry("380x450+550+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="white",bg="black")
                l.place(x=0,y=10, height=50,relwidth=1)


                name_lbl=Label(self.root2,text="Contact",font=("timesnew romans" ,12,"bold"),fg="purple")
                name_lbl.place(x=50,y=100)

                self.txtcontact=Entry(self.root2,font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
                self.txtcontact.place(x=50,y=140,width=300)


                newpassword_lbl=Label(self.root2,text="New Password",font=("timesnew romans" ,12,"bold"),fg="purple")
                newpassword_lbl.place(x=50,y=180)

                self.txtlpass=Entry(self.root2,font=("timesnew romans" ,14,"bold"),fg="purple")
                self.txtlpass.place(x=50,y=220,width=300)

                resetbtn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="purple",activeforeground="white",activebackground="red")
                resetbtn.place(x=200,y=300,width=120,height=35)



           

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system") 

        
        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()

        img3=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\reg.jpg")
        img3=img3.resize((1530,920),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=700)
        #left image

        img=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\re.jpg")
        img=img.resize((1530,920),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=50,y=80,width=450,height=550)

        #reg1_lbl=Label(text="Face Recogination",font=("timesnew romans" ,25,"bold"),fg="purple")
        #reg1_lbl.place(x=130,y=300)

        #reg1_lbl=Label(text="Attendence System",font=("timesnew romans" ,25,"bold"),fg="purple")
        #reg1_lbl.place(x=130,y=360)

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=80,width=800,height=550)

        #label
       
        reg_lbl=Label(frame,text="Register Here",font=("timesnew romans" ,20,"bold"),fg="purple",bg="white")
        reg_lbl.place(x=300,y=30)

        firstname_lbl=Label(frame,text="Firstname",font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
        firstname_lbl.place(x=70,y=120)

        self.txtfname=Entry(frame,textvariable=self.var_fname,font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
        self.txtfname.place(x=70,y=160,width=270)

        lastname_lbl=Label(frame,text="Lastname",font=("timesnew romans" ,12,"bold"),fg="purple",bg="white")
        lastname_lbl.place(x=450,y=120)

        self.txtlname=Entry(frame,textvariable=self.var_lname,font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
        self.txtlname.place(x=450,y=160,width=270)

        contact_lbl=Label(frame,text="Contact",font=("timesnew romans" ,12,"bold"),fg="purple",bg="white")
        contact_lbl.place(x=70,y=230)

        self.txtcontact=Entry(frame,textvariable=self.var_contact,font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
        self.txtcontact.place(x=70,y=260,width=270)

        email_lbl=Label(frame,text="Email",font=("timesnew romans" ,12,"bold"),fg="purple",bg="white")
        email_lbl.place(x=450,y=230)

        self.txtemail=Entry(frame,textvariable=self.var_email,font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
        self.txtemail.place(x=450,y=260,width=270)

        password_lbl=Label(frame,text="Password",font=("timesnew romans" ,12,"bold"),fg="purple",bg="white")
        password_lbl.place(x=70,y=320)

        self.txtPassword=Entry(frame,textvariable=self.var_password,font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
        self.txtPassword.place(x=70,y=360,width=270)

        confirmpassword_lbl=Label(frame,text="ConfirmPassword",font=("timesnew romans" ,12,"bold"),fg="purple",bg="white")
        confirmpassword_lbl.place(x=450,y=320)

        self.txtcPassword=Entry(frame,textvariable=self.var_cpassword,font=("timesnew romans" ,14,"bold"),fg="purple",bg="white")
        self.txtcPassword.place(x=450,y=360,width=270)

        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame, variable=self.var_check,text="I agree all terms and conditon",font=("timesnew romans" ,12,"bold"),fg="purple",bg="white")
        checkbtn.place(x=70,y=420)

        registerbtn=Button(frame,text="Register Now",command=self.register_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="purple",activeforeground="white",activebackground="red")
        registerbtn.place(x=180,y=480,width=120,height=35)

        loginbtn=Button(frame,text="Login Now",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="purple",activeforeground="white",activebackground="red")
        loginbtn.place(x=450,y=480,width=120,height=35)



    def register_data(self):
        if self.var_fname.get()=="" or self.var_email=="Select":
            messagebox.showerror("Error","All field are required")

        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","password and comfirm password must be same")

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@purnaale#1633",database="face_recogination_attentdance")
            my_cursor=conn.cursor()
            query=("select * from register1 where email = %s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                    messagebox.showerror("Eror","user already exit, please try another email to register")

            else:
                     my_cursor.execute("insert into register1 values(%s,%s,%s,%s,%s,%s)",(
                                        self.var_fname.get(),
                                        self.var_lname.get(),
                                        self.var_contact.get(),
                                        self.var_email.get(),
                                        self.var_password.get(),
                                        self.var_cpassword.get(),

            
                ))
            conn.commit()
            conn.close()
               
            messagebox.showinfo("Success","register successfully",parent=self.root)



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
    main()