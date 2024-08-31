from tkinter import*
from tkinter import ttk, PhotoImage
from PIL import Image,ImageTk,ImageFilter
from tkinter import messagebox
import mysql.connector
from main import FRS

class REG:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1540x920+0+0")

        self.var_user=StringVar()
        self.var_passwd=StringVar()
        self.var_email=StringVar()
        self.var_conpass=StringVar()

        img=Image.open("E:/adeebs_lab_codes/python_project/images/bg_3.jpg")
        img=img.resize((1540,920),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(img)

        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)

        main_frame=Frame(bg,bd=2,bg="#FCFCFC")
        main_frame.place(x=605,y=210,width=340,height=450)

        img1=Image.open("E:/adeebs_lab_codes/python_project/images/profile.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(img1)

        l1=Label(image=self.img1,bg="black",borderwidth=0)
        l1.place(x=730,y=220,width=100,height=100)

        get_str=Label(main_frame,text="   Register   ",font=("times new roman",18,"bold"),fg="white",bg="black")
        get_str.place(x=105,y=100)

        user_l=Label(main_frame,text="Username",font=("times new roman",12,"bold"),fg="black",bg="#FCFCFC")
        user_l.place(x=10,y=155)

        self.txtuser=ttk.Entry(main_frame,textvariable=self.var_user,font=("times new roman",12,"bold"))
        self.txtuser.place(x=90,y=155,width=230)

        email_l=Label(main_frame,text="Emial ID",font=("times new roman",12,"bold"),fg="black",bg="#FCFCFC")
        email_l.place(x=10,y=200)

        self.txtemail=ttk.Entry(main_frame,textvariable=self.var_email,font=("times new roman",12,"bold"))
        self.txtemail.place(x=90,y=200,width=230)

        pass_l=Label(main_frame,text="Password",font=("times new roman",12,"bold"),fg="black",bg="#FCFCFC")
        pass_l.place(x=10,y=245)

        self.txtpass=ttk.Entry(main_frame,textvariable=self.var_passwd,font=("times new roman",12,"bold"))
        self.txtpass.place(x=90,y=245,width=230)

        cpass_l=Label(main_frame,text="Conform",font=("times new roman",12,"bold"),fg="black",bg="#FCFCFC")
        cpass_l.place(x=10,y=280)

        cpass_l=Label(main_frame,text="Password",font=("times new roman",12,"bold"),fg="black",bg="#FCFCFC")
        cpass_l.place(x=10,y=300)

        self.txtcpass=ttk.Entry(main_frame,textvariable=self.var_conpass,font=("times new roman",12,"bold"))
        self.txtcpass.place(x=90,y=290,width=230)

        #button
        self.var_check=IntVar()
        che=Checkbutton(main_frame,variable=self.var_check,text="I agree to the terms & conditions",font=("times new roman",12),fg="black",bg="#FCFCFC")
        che.place(x=10,y=330)

        regbtn=Button(main_frame,text="Register",command=self.reg_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="cyan2",activeforeground="white",activebackground="cyan2")
        regbtn.place(x=110,y=370,width=120,height=35)

        pass_l=Label(main_frame,text="Already have an account?",font=("times new roman",10),fg="black",bg="#FCFCFC")
        pass_l.place(x=80,y=410)

        albtn=Button(main_frame,text="Login",command=self.return_log,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="#FCFCFC",activeforeground="black",activebackground="#FCFCFC")
        albtn.place(x=225,y=410)

    def reg_data(self):
        if self.var_user.get()=="" or self.var_email.get()=="" or self.var_passwd.get()=="" or self.var_conpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_passwd.get()!=self.var_conpass.get():
            messagebox.showerror("Error","Password and Confirm Password are not same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plaese agree to the terms & conditions")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
                my_cur=conn.cursor()
                query=("select * from register where Email=%s and Username=%s")
                value=(self.var_email.get(),self.var_user.get(),)
                my_cur.execute(query,value)
                row=my_cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User Or Email already exist, please try another username or Email",parent=self.root)
                else:
                    my_cur.execute("insert into register values(%s,%s,%s)",(
                        self.var_user.get(),
                        self.var_email.get(),
                        self.var_passwd.get()
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Data Registered",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def return_log(self):
        self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj= REG(root)
    root.mainloop()