from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class US:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x920+0+0")
        self.root.title("Face Recognition System")

        img=Image.open("E:/adeebs_lab_codes/python_project/images/bg.jpg")
        img=img.resize((1540,920),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(img)

        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,width=1540,height=920)

        fl1=Label(bg,text="About Us",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl1.place(x=0,y=0,width=1540,height=55)

        main_frame=Frame(bg,bd=2,bg="white")
        main_frame.place(x=20,y=65,width=1490,height=760)

        dev_lab=Label(main_frame,text="Hello world this is our project",font=("times new roman",12,"bold"),bg="white")
        dev_lab.place(x=0,y=5)



if __name__=="__main__":
    root=Tk()
    obj= US(root)
    root.mainloop()