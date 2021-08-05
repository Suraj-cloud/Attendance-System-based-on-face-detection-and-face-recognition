from tkinter import*
from tkinter import ttk
from typing import Dict
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1370x790+0+0")
        self.root.title("Attendance System")

        #=========================variable=========================

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



        # first image
        img=Image.open("attendance11.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg) 
        f_lbl.place(x=0,y=0,width=500,height=150)

        # second image
        img2=Image.open("attendance12.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2) 
        f_lbl.place(x=500,y=0,width=450,height=150)

        # third image
        img3=Image.open("train_bottom.jpg")
        img3=img3.resize((500,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=950,y=0,width=500,height=150)

        # bg image
        img4=Image.open("bgimage.jpg")
        img4=img4.resize((1500,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4) 
        bg_img.place(x=0,y=150,width=1370,height=570)

         # title

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="light grey",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1370,height=45)

         #frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1,y=50,width=1360,height=520)

        # left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=2,width=665,height=510)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=2,width=660,height=485)

        #  image
        img5=Image.open("train_bottom.jpg")
        img5=img5.resize((658,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(self.root,image=self.photoimg5)
        f_lbl.place(x=12,y=230,width=658,height=200)



        # label and entry

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=205,width=660,height=280)

        # Attendance Id
        attendanceID_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold",),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold",),bg="white")
        roll_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=1,pady=10,sticky=W)

        # Name
        namelabel=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold",),bg="white")
        namelabel.grid(row=1,column=0,padx=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold",),bg="white")
        dep_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=1,pady=10,sticky=W)

        # Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold",),bg="white")
        time_label.grid(row=2,column=0,padx=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold",),bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=1,pady=10,sticky=W)


        

        #Attendance

        attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold",),bg="white")
        attendance_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20,font=("times new roman",11, "bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # button Frame

        Button_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        Button_frame.place(x=1,y=210,width=655,height=37)  

        # save button

        save_button=Button(Button_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        # update button

        update_button=Button(Button_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        # Delete button

        Delete_button=Button(Button_frame,text="Update",command=self.action,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        Delete_button.grid(row=0,column=2)

        # reset button

        reset_button=Button(Button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)
       
        # right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=676,y=2,width=667,height=510) 

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=2,width=663,height=483)

        #======================scroll bar table======================

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendace ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


#=================fetch data========================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    # Update 
    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #reset

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()