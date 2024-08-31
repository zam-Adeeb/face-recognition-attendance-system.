from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import tkinter
import numpy as np
from std import STD
from attend import ATT
from aboutus import US
# from face import FAE



class FRS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x920+0+0")
        self.root.title("Face Recognition System")

        # images
        imgbg=Image.open("E:/adeebs_lab_codes/python_project/images/bg.jpg")
        imgbg=imgbg.resize((1540,920),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(imgbg)

        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,width=1540,height=920)

        fl1=Label(bg,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl1.place(x=0,y=0,width=1540,height=55)

        # button1
        img1=Image.open("E:/adeebs_lab_codes/python_project/images/1.jpg")
        img1=img1.resize((250,220),Image.LANCZOS)
        self.col1=ImageTk.PhotoImage(img1)

        b1=Button(bg,image=self.col1,command=self.std_det,cursor="hand2")
        b1.place(x=300,y=100,width=250,height=220)

        b1_1=Button(bg,text="Student Details",command=self.std_det,cursor="hand2",font=("times new roman",20,"bold"),bg="navy",fg="white")
        b1_1.place(x=300,y=300,width=250,height=40)

        # button2
        img2=Image.open("E:/adeebs_lab_codes/python_project/images/3.jpg")
        img2=img2.resize((250,220),Image.LANCZOS)
        self.col2=ImageTk.PhotoImage(img2)

        b2=Button(bg,image=self.col2,cursor="hand2",command=self.face_recong)
        b2.place(x=650,y=100,width=250,height=220)

        b2_1=Button(bg,text="Face Detector",cursor="hand2",command=self.face_recong,font=("times new roman",20,"bold"),bg="navy",fg="white")
        b2_1.place(x=650,y=300,width=250,height=40)

        # button3
        img3=Image.open("E:/adeebs_lab_codes/python_project/images/5.jpg")
        img3=img3.resize((250,220),Image.LANCZOS)
        self.col3=ImageTk.PhotoImage(img3)

        b3=Button(bg,image=self.col3,cursor="hand2",command=self.att_det)
        b3.place(x=1000,y=100,width=250,height=220)

        b3_1=Button(bg,text="Student Attendance",cursor="hand2",command=self.att_det,font=("times new roman",20,"bold"),bg="navy",fg="white")
        b3_1.place(x=1000,y=300,width=250,height=40)

        # button4
        # img4=Image.open("E:/adeebs_lab_codes/python_project/images/10.jpg")
        # img4=img4.resize((250,220),Image.LANCZOS)
        # self.col4=ImageTk.PhotoImage(img4)

        # b4=Button(bg,image=self.col4,cursor="hand2")
        # b4.place(x=1100,y=100,width=250,height=220)

        # b4_1=Button(bg,text="Teacher Attendance",cursor="hand2",font=("times new roman",20,"bold"),bg="navy",fg="white")
        # b4_1.place(x=1100,y=300,width=250,height=40)

        # button5
        img5=Image.open("E:/adeebs_lab_codes/python_project/images/4.jpg")
        img5=img5.resize((250,220),Image.LANCZOS)
        self.col5=ImageTk.PhotoImage(img5)

        b5=Button(bg,image=self.col5,cursor="hand2",command=self.train_data)
        b5.place(x=300,y=400,width=250,height=220)

        b5_1=Button(bg,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="navy",fg="white")
        b5_1.place(x=300,y=600,width=250,height=40)

        # button6
        img6=Image.open("E:/adeebs_lab_codes/python_project/images/7.jpg")
        img6=img6.resize((250,220),Image.LANCZOS)
        self.col6=ImageTk.PhotoImage(img6)

        b6=Button(bg,image=self.col6,cursor="hand2",command=self.open_img)
        b6.place(x=650,y=400,width=250,height=220)

        b6_1=Button(bg,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="navy",fg="white")
        b6_1.place(x=650,y=600,width=250,height=40)

        # button7
        img7=Image.open("E:/adeebs_lab_codes/python_project/images/2.jpg")
        img7=img7.resize((250,220),Image.LANCZOS)
        self.col7=ImageTk.PhotoImage(img7)

        b7=Button(bg,image=self.col7,cursor="hand2",command=self.abus)
        b7.place(x=1000,y=400,width=250,height=220)

        b7_1=Button(bg,text="Dev",cursor="hand2",command=self.abus,font=("times new roman",20,"bold"),bg="navy",fg="white")
        b7_1.place(x=1000,y=600,width=250,height=40)

        # button8
        # img8=Image.open("E:/adeebs_lab_codes/python_project/images/8.jpg")
        # img8=img8.resize((250,220),Image.LANCZOS)
        # self.col8=ImageTk.PhotoImage(img8)

        # b8=Button(bg,image=self.col8,cursor="hand2")
        # b8.place(x=1100,y=400,width=250,height=220)

        # b8_1=Button(bg,text="Emotion Detector",cursor="hand2",font=("times new roman",20,"bold"),bg="navy",fg="white")
        # b8_1.place(x=1100,y=600,width=250,height=40)
        
        b9=Button(bg,text="EXIT",cursor="hand2",command=self.iexit,font=("times new roman",20,"bold"),bg="navy",fg="white")
        b9.place(x=650,y=700,width=240,height=40)

        # Function
        self.recognized_faces = set()
        now = datetime.now()
        self.filename = now.strftime("Attendance_%d-%m-%Y_%H-%M-%S.csv")

    def std_det(self): #student detalis 
        self.new_window=Toplevel(self.root)
        self.app=STD(self.new_window)

    def att_det(self): #student attendance detalis 
        self.new_window=Toplevel(self.root)
        self.app=ATT(self.new_window)

    def face_det(self): #student attendance detalis 
        self.new_window=Toplevel(self.root)
        self.app=FAE(self.new_window)

    def open_img(self): #open img folder
        os.startfile("E:/adeebs_lab_codes/python_project/data")

    def abus(self): #student attendance detalis 
        self.new_window=Toplevel(self.root)
        self.app=US(self.new_window)

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recongnition","Are you sure",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return

    def train_data(self): #training the data
        data_dir=("E:/adeebs_lab_codes/python_project/data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            img_np=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training Data",img_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("E:/adeebs_lab_codes/python_project/classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")

    def mark_att(self,i,j,k,n): #attendence
        with open(f"E:/adeebs_lab_codes/python_project/Attendance/{self.filename}", "a", newline="\n") as f:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            d2 = now.strftime("%H:%M:%S")
            f.writelines(f"\n{n},{i},{k},{j},{d2},{d1},Present")
        # with open("E:/adeebs_lab_codes/python_project/Attendance.csv","r+",newline="\n") as f:
            # my_data=f.readlines()
            # name_list=[]
            # for line in my_data:
            #     entry=line.split((","))
            #     name_list.append(entry[0])
            # if((i not in name_list) and (j not in name_list) and (k not in name_list)) :
                # now=datetime.now()
                # d1=now.strftime("%d/%m/%Y")
                # d2=now.strftime("%H:%M:%S")
                # f.writelines(f"\n{n},{i},{k},{j},{d2},{d1},Present")

    
    def face_recong(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                # conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
                # my_cur=conn.cursor()
                # my_cur.execute("select Name from student where sid="+str(id))
                # n=my_cur.fetchone()
                # n="+".join(n)

                # my_cur.execute("select usn from student where sid="+str(id))
                # r=my_cur.fetchone()
                # r="+".join(r)

                # my_cur.execute("select Dept from student where sid="+str(id))
                # d=my_cur.fetchone()
                # d="+".join(d)

                # my_cur.execute("select sid from student where sid="+str(id))
                # i=my_cur.fetchone()
                # i="+".join(i)

                if id not in self.recognized_faces:
                    self.recognized_faces.add(id)
                    conn = mysql.connector.connect(host="localhost", username="root", password="0000", database="face_atd")
                    my_cur = conn.cursor()

                    my_cur.execute("select Name from student where sid=%s", (id,))
                    n = my_cur.fetchone()
                    if n:
                        n = "+".join(n)

                    my_cur.execute("select usn from student where sid=%s", (id,))
                    r = my_cur.fetchone()
                    if r:
                        r = "+".join(r)

                    my_cur.execute("select Dept from student where sid=%s", (id,))
                    d = my_cur.fetchone()
                    if d:
                        d = "+".join(d)

                    my_cur.execute("select sid from student where sid=%s", (id,))
                    i = my_cur.fetchone()
                    if i:
                        i = "+".join(i)

                    if confidence>77:
                        cv2.putText(img,f"USN:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_att(r,n,d,i)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    self.recognized_faces.add(id)
                    conn = mysql.connector.connect(host="localhost", username="root", password="0000", database="face_atd")
                    my_cur = conn.cursor()

                    my_cur.execute("select Name from student where sid=%s", (id,))
                    n = my_cur.fetchone()
                    n = "+".join(n)

                    my_cur.execute("select usn from student where sid=%s", (id,))
                    r = my_cur.fetchone()
                    r = "+".join(r)

                    my_cur.execute("select Dept from student where sid=%s", (id,))
                    d = my_cur.fetchone()
                    d = "+".join(d)

                    my_cur.execute("select sid from student where sid=%s", (id,))
                    i = my_cur.fetchone()
                    i="+".join(i)

                    if confidence>77:
                        cv2.putText(img,f"USN:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            # self.mark_att(r,n,d,i)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("E:/adeebs_lab_codes/python_project/haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("E:/adeebs_lab_codes/python_project/classifier.xml")

        vid_cap=cv2.VideoCapture(0)
        while True:
            ret,img=vid_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if (cv2.waitKey(1)==ord('q')):
                break
        vid_cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj= FRS(root)
    root.mainloop()