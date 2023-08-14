
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

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
        # reg1_lbl.place(x=130,y=360)

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
            



if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()