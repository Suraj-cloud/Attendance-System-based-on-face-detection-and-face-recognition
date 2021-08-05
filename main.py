from tkinter import*
from tkinter import ttk
import tkinter 
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class face_Recognition_System:
       def __init__(self,root):
           self.root=root
           self.root.geometry("1370x790+0+0")
           self.root.title("Face Recognition System")

            # first image
           img=Image.open("facial.jpg")
           img=img.resize((470,130),Image.ANTIALIAS)
           self.photoimg=ImageTk.PhotoImage(img)

           f_lbl=Label(self.root,image=self.photoimg)
           f_lbl.place(x=0,y=0,width=470,height=130)

           #second Image
           img1=Image.open("train_top.png")
           img1=img1.resize((490,130),Image.ANTIALIAS)
           self.photoimg1=ImageTk.PhotoImage(img1)

           f_lbl=Label(self.root,image=self.photoimg1)
           f_lbl.place(x=470,y=0,width=490,height=130)

             #third image
           img2=Image.open("recognition.jpg")
           img2=img2.resize((540,130),Image.ANTIALIAS)
           self.photoimg2=ImageTk.PhotoImage(img2)

           f_lbl=Label(self.root,image=self.photoimg2)
           f_lbl.place(x=960,y=0,width=540,height=130)

            #bg image
           img3=Image.open("bgimage.jpg")
           img3=img3.resize((1530,710),Image.ANTIALIAS)
           self.photoimg3=ImageTk.PhotoImage(img3)

           bg_img=Label(self.root,image=self.photoimg3)
           bg_img.place(x=0,y=130,width=1530,height=710)

           title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="light green",fg="blue")
           title_lbl.place(x=0,y=0,width=1370,height=45)

           #====================time=================

           def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

           lbl= Label(title_lbl, font=('times new roman',14,'bold'),background='Light green',foreground='blue')
           lbl.place(x=0,y=0,width=110,height=50)
           time()

          
           #student button
           img4=Image.open("student.jpg")
           img4=img4.resize((220,220),Image.ANTIALIAS)
           self.photoimg4=ImageTk.PhotoImage(img4)

           b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
           b1.place(x=150,y=80,width=220,height=220)

           b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=150,y=280,width=220,height=40)

           #detect face button
           img5=Image.open("detector.jfif")
           img5=img5.resize((220,220),Image.ANTIALIAS)
           self.photoimg5=ImageTk.PhotoImage(img5)

           b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
           b1.place(x=450,y=80,width=220,height=220)

           b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=450,y=280,width=220,height=40)

           #attendace button
           img6=Image.open("attendance1.jpg")
           img6=img6.resize((220,220),Image.ANTIALIAS)
           self.photoimg6=ImageTk.PhotoImage(img6)

           b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
           b1.place(x=750,y=80,width=220,height=220)

           b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=750,y=280,width=220,height=40)

            #help button
           img7=Image.open("help.jpg")
           img7=img7.resize((220,220),Image.ANTIALIAS)
           self.photoimg7=ImageTk.PhotoImage(img7)

           b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
           b1.place(x=1050,y=80,width=220,height=220)

           b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=1050,y=280,width=220,height=40)
 
            #train button
           img8=Image.open("traindata.webp")
           img8=img8.resize((220,220),Image.ANTIALIAS)
           self.photoimg8=ImageTk.PhotoImage(img8)

           b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
           b1.place(x=150,y=350,width=220,height=220)

           b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=150,y=550,width=220,height=40)

            #photos button
           img9=Image.open("images.jpg")
           img9=img9.resize((220,220),Image.ANTIALIAS)
           self.photoimg9=ImageTk.PhotoImage(img9)

           b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
           b1.place(x=450,y=350,width=220,height=220)

           b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=450,y=550,width=220,height=40)

            # developer button
           img10=Image.open("developer.jpg")
           img10=img10.resize((220,220),Image.ANTIALIAS)
           self.photoimg10=ImageTk.PhotoImage(img10)

           b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
           b1.place(x=750,y=350,width=220,height=220)

           b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=750,y=550,width=220,height=40)

           # exit button
           img11=Image.open("exit.jpg")
           img11=img11.resize((220,220),Image.ANTIALIAS)
           self.photoimg11=ImageTk.PhotoImage(img11)

           b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
           b1.place(x=1050,y=350,width=220,height=220)

           b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg="blue",fg="white")
           b1_1.place(x=1050,y=550,width=220,height=40)
      
       def open_img(self):
         os.startfile("DATA")

       def iexit(self):
         self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
         if self.iexit>0:
           self.root.destroy()
         else:
           return
#=====================functions buttons========================
       def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window) 

       def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window) 

       def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)

       def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)

       def developer_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)
       
       def help_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Help(self.new_window)


if __name__ =="__main__":
    root=Tk()
    obj=face_Recognition_System(root)
    root.mainloop()