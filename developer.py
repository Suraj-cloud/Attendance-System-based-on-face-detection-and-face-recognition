from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox


class Developer:
       def __init__(self,root):
           self.root=root
           self.root.geometry("1370x790+0+0")
           self.root.title("Face Recognition System")

           title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="light green",fg="blue")
           title_lbl.place(x=0,y=0,width=1370,height=55)

           img_top=Image.open("dev.jpg")
           img_top=img_top.resize((1370,720),Image.ANTIALIAS)
           self.photoimg_top=ImageTk.PhotoImage(img_top)

           f_lbl=Label(self.root,image=self.photoimg_top)
           f_lbl.place(x=0,y=55,width=1370,height=720)

           #Frame
           main_frame=Frame(f_lbl,bd=2,bg="sky blue")
           main_frame.place(x=865,y=-1,width=500,height=600)

           img_top1=Image.open("Photo.jpeg")
           img_top1=img_top1.resize((200,215),Image.ANTIALIAS)
           self.photoimg_top1=ImageTk.PhotoImage(img_top1)

           f_lbl=Label(main_frame,image=self.photoimg_top1)
           f_lbl.place(x=300,y=-2,width=200,height=215)

           #Developer info
           dev_label=Label(main_frame,text="Suraj Phatangare",font=("Lucida Calligraphy",20,"bold"),fg="black",bg="sky blue")
           dev_label.place(x=0,y=5)

           dev_label=Label(main_frame,text="E&TC",font=("Lucida Calligraphy",10,"bold"),fg="black",bg="sky blue")
           dev_label.place(x=0,y=40)

           dev_label=Label(main_frame,text="SIEM, Nashik",font=("Lucida Calligraphy",10,"bold"),fg="black",bg="sky blue")
           dev_label.place(x=0,y=60)



           img=Image.open("dev1.jpg")
           img=img.resize((500,390),Image.ANTIALIAS)
           self.photoimg=ImageTk.PhotoImage(img)

           f_lbl=Label(main_frame,image=self.photoimg)
           f_lbl.place(x=0,y=210,width=500,height=390)




          


if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()