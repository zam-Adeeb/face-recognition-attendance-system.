from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import cv2
import os
import csv

mydata=[]

class ATT:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x920+0+0")
        self.root.title("Face Recognition System")

        self.var_usn=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_id=StringVar()
        self.var_att=StringVar()

        img=Image.open("E:/adeebs_lab_codes/python_project/images/bg2.jpg")
        img=img.resize((1540,920),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(img)

        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,width=1540,height=920)

        fl1=Label(bg,text="Student Management System",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl1.place(x=0,y=0,width=1540,height=55)

        main_frame=Frame(bg,bd=2,bg="white")
        main_frame.place(x=20,y=65,width=1490,height=760)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE)
        Left_frame.place(x=10,y=10,width=600,height=700)

        fl2=Label(Left_frame,text="Student Information",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl2.place(x=10,y=10,width=575,height=55)

        Cs_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        Cs_frame.place(x=20,y=80,width=565,height=480)

        temp=Label(Cs_frame,text="",font=("times new roman",12,"bold"),bg="white")
        temp.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        usn_l=Label(Cs_frame,text="USN",font=("times new roman",12,"bold"),bg="white")
        usn_l.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        usn_in=ttk.Entry(Cs_frame,textvariable=self.var_usn,width=22,font=("times new roman",12,"bold"))
        usn_in.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        n_l=Label(Cs_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        n_l.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        n_in=ttk.Entry(Cs_frame,textvariable=self.var_name,width=22,font=("times new roman",12,"bold"))
        n_in.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        id_l=Label(Cs_frame,text="ID No",font=("times new roman",12,"bold"),bg="white")
        id_l.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        id_in=ttk.Entry(Cs_frame,textvariable=self.var_id,width=22,font=("times new roman",12,"bold"))
        id_in.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        Dept_l=Label(Cs_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        Dept_l.grid(row=4,column=0,padx=10)

        dep=ttk.Combobox(Cs_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep["values"]=("Select Department","CSE","ISE","ECE","EEE","Physics","Chemistry")
        dep.current(0)
        dep.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        d_l=Label(Cs_frame,text="Data",font=("times new roman",12,"bold"),bg="white")
        d_l.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        d_in=ttk.Entry(Cs_frame,textvariable=self.var_date,width=22,font=("times new roman",12,"bold"))
        d_in.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        t_l=Label(Cs_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        t_l.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        t_in=ttk.Entry(Cs_frame,textvariable=self.var_time,width=22,font=("times new roman",12,"bold"))
        t_in.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        att_l=Label(Cs_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        att_l.grid(row=7,column=0,padx=10)

        a_s=ttk.Combobox(Cs_frame,textvariable=self.var_att,font=("times new roman",12,"bold"),width=20,state="readonly")
        a_s["values"]=("Select Status","Present","Absent")
        a_s.current(0)
        a_s.grid(row=7,column=1,padx=2,pady=10,sticky=W)

        #button
        B_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        B_frame.place(x=20,y=570,width=565,height=100)

        b3=Button(B_frame,text="import csv",width=17,command=self.ImportCvs,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b3.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        # b4=Button(B_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # b4.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        b5=Button(B_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b5.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        b6=Button(B_frame,text="Export csv",width=17,command=self.ExportCvs,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b6.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        # Right
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,)
        Right_frame.place(x=640,y=10,width=820,height=700)

        fl3=Label(Right_frame,text="Student Database",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl3.place(x=10,y=10,width=800,height=55)

        # Table
        T_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        T_frame.place(x=10,y=80,width=800,height=600)

        sr_x=ttk.Scrollbar(T_frame,orient=HORIZONTAL)
        sr_y=ttk.Scrollbar(T_frame,orient=VERTICAL)
        self.st=ttk.Treeview(T_frame,columns=("Id","USN","Dept","Name","Time","Date","Attendance"),xscrollcommand=sr_x.set,yscrollcommand=sr_y.set)
        sr_x.pack(side=BOTTOM,fill=X)
        sr_y.pack(side=RIGHT,fill=Y)
        sr_x.config(command=self.st.xview)
        sr_y.config(command=self.st.yview)

        self.st.heading("Id",text="ID")
        self.st.heading("USN",text="USN")
        self.st.heading("Dept",text="Dept")
        self.st.heading("Name",text="Name")
        self.st.heading("Time",text="Time")
        self.st.heading("Date",text="Date")
        self.st.heading("Attendance",text="Attendance")

        self.st["show"]="headings"

        self.st.column("Id",width=100)
        self.st.column("Name",width=100)
        self.st.column("USN",width=100)
        self.st.column("Dept",width=100)
        self.st.column("Time",width=100)
        self.st.column("Date",width=100)
        self.st.column("Attendance",width=100)
        
        self.st.pack(fill=BOTH,expand=1)
        self.st.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
            self.st.delete(*self.st.get_children())
            for i in rows:
                self.st.insert("",END,values=i)
    
    def ImportCvs(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def ExportCvs(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_focus=self.st.focus()
        cont=self.st.item(cursor_focus)
        data=cont["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_usn.set(data[2]),
        self.var_dept.set(data[3]),
        self.var_date.set(data[4]),
        self.var_time.set(data[5]),
        self.var_att.set(data[6])

    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_usn.set("")
        self.var_dept.set("Select Department")
        self.var_date.set("")
        self.var_time.set("")
        self.var_att.set("Select Status")




if __name__=="__main__":
    root=Tk()
    obj=ATT(root)
    root.mainloop()