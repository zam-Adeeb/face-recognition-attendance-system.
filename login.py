from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import FRS
from reg import REG

class LOG:
    def __init__(self,root):
        self.root = root
        self.root.title("login")
        self.root.geometry("1540x920+0+0")

        img=Image.open("E:/adeebs_lab_codes/python_project/images/bg_3.jpg")
        img=img.resize((1540,920),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(img)

        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)

        main_frame=Frame(bg,bd=2,bg="#FCFCFC")
        main_frame.place(x=600,y=220,width=340,height=400)

        img1=Image.open("E:/adeebs_lab_codes/python_project/images/profile.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(img1)

        l1=Label(image=self.img1,bg="black",borderwidth=0)
        l1.place(x=730,y=230,width=100,height=100)

        get_str=Label(main_frame,text="    Login     ",font=("times new roman",18,"bold"),fg="white",bg="black")
        get_str.place(x=115,y=100)

        user_l=Label(main_frame,text="Username",font=("times new roman",12,"bold"),fg="black",bg="#FCFCFC")
        user_l.place(x=10,y=155)

        self.txtuser=ttk.Entry(main_frame,font=("times new roman",12,"bold"))
        self.txtuser.place(x=90,y=155,width=230)

        pass_l=Label(main_frame,text="Password",font=("times new roman",12,"bold"),fg="black",bg="#FCFCFC")
        pass_l.place(x=10,y=210)

        self.txtpass=ttk.Entry(main_frame,font=("times new roman",12,"bold"))
        self.txtpass.place(x=90,y=210,width=230)

        self.var_check=IntVar()
        che=Checkbutton(main_frame,variable=self.var_check,text="Remember me",font=("times new roman",12),fg="black",bg="#FCFCFC")
        che.place(x=10,y=260)

        # login button
        logbtn=Button(main_frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="cyan2",activeforeground="white",activebackground="cyan2")
        logbtn.place(x=110,y=300,width=120,height=35)

        pass_l=Label(main_frame,text="Already have an account?",font=("times new roman",10),fg="black",bg="#FCFCFC")
        pass_l.place(x=80,y=350)

        albtn=Button(main_frame,text="Login",command=self.reg_win,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="#FCFCFC",activeforeground="black",activebackground="#FCFCFC")
        albtn.place(x=225,y=350)

        passbtn=Button(main_frame,text="Forgot Password",font=("times new roman",12),borderwidth=0,fg="black",bg="#FCFCFC",activeforeground="black",activebackground="#FCFCFC")
        passbtn.place(x=200,y=260,width=120)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="AAB" and self.txtpass.get()=="zero":
            messagebox.showinfo("Success","Welcome to the Face Reconigtion System")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
                my_cur=conn.cursor()
                my_cur.execute("select * from register where Username=%s and Password=%s",(
                    self.txtuser.get(),
                    self.txtpass.get()
                ))
                row=my_cur.fetchone()
                if row==NONE:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                else:
                    open_main=messagebox.askyesno("YesNO","Assess only Admin")
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=FRS(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



    def reg_win(self):
        self.new_window=Toplevel(self.root)
        self.app=REG(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj= LOG(root)
    root.mainloop()