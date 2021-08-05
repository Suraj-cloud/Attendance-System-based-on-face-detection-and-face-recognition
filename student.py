from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1370x790+0+0")
        self.root.title("face Recognition System")


        #********************Variables********************

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        


        # first image
        img=Image.open("student1.png")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg) 
        f_lbl.place(x=0,y=0,width=500,height=150)

        # second image
        img2=Image.open("student2.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2) 
        f_lbl.place(x=500,y=0,width=450,height=150)

        # third image
        img3=Image.open("student3.png")
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


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="pink",fg="dark green")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        
        
        
        #frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1,y=50,width=1360,height=520)

        # left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=2,width=665,height=510)  

            

        # current course information

        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=2,y=5,width=659,height=120)  

        # department

        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold",),bg="white")
        dep_label.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","E&TC","Computer","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course

        course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold",),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year

        year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold",),bg="white")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester

        semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold",),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)

        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student information

        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class_Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=2,y=125,width=659,height=500) 

        # Student ID

        studentID_label=Label(Class_Student_frame,text="Student ID:",font=("times new roman",12,"bold",),bg="white")
        studentID_label.grid(row=0,column=0,padx=5,sticky=W)

        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Student name

        studentname_label=Label(Class_Student_frame,text="Student Name:",font=("times new roman",12,"bold",),bg="white")
        studentname_label.grid(row=0,column=2,padx=5,sticky=W)

        studentname_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Class Division

        Class_div_label=Label(Class_Student_frame,text="Class Division:",font=("times new roman",12,"bold",),bg="white")
        Class_div_label.grid(row=1,column=0,padx=5,sticky=W)

        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # Roll no

        Roll_no_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman",12,"bold",),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=5,sticky=W)

        Roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Gender

        Gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",12,"bold",),bg="white")
        Gender_label.grid(row=2,column=0,padx=5,sticky=W)
        
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)


        # DOB

        dob_label=Label(Class_Student_frame,text="DOB:",font=("times new roman",12,"bold",),bg="white")
        dob_label.grid(row=2,column=2,padx=5,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        # Email

        email_label=Label(Class_Student_frame,text="Email:",font=("times new roman",12,"bold",),bg="white")
        email_label.grid(row=3,column=0,padx=5,sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # Phone no

        Phone_no_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman",12,"bold",),bg="white")
        Phone_no_label.grid(row=3,column=2,padx=5,sticky=W)

        Phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        Phone_no_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        # Address

        Address_label=Label(Class_Student_frame,text="Address:",font=("times new roman",12,"bold",),bg="white")
        Address_label.grid(row=4,column=0,padx=5,sticky=W)

        Address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        # Teacher Name

        Teacher_name_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold",),bg="white")
        Teacher_name_label.grid(row=4,column=2,padx=5,sticky=W)

        Teacher_name_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        Teacher_name_entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        # Radio Bottons

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

       
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=10)

        # button Frame

        Button_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        Button_frame.place(x=5,y=400,width=655,height=70)  

        # save button

        save_button=Button(Button_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        # update button

        update_button=Button(Button_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        # Delete button

        Delete_button=Button(Button_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        Delete_button.grid(row=0,column=2)

        # reset button

        reset_button=Button(Button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)

        # take a photo sample button

        take_photo_button=Button(Button_frame,text="Take Photo Sample",command=self.generate_dataset,width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        take_photo_button.grid(row=1,column=1)

        # Update photo button

        update_button=Button(Button_frame,text="Update Photo Sample",width=17,font=("times new roman",12,"bold",),bg="blue",fg="white")
        update_button.grid(row=1,column=2)

        # right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=676,y=2,width=667,height=510) 

        # *************************SEARCH SYSTEM*********************************

        Search_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=676,y=2,width=667,height=70) 

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold",),bg="light green",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=14,state="readonly")
        search_combo["values"]=("Select","Roll No","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        search_button=Button(Search_frame,text="Search",command=self.search_data,width=14,font=("times new roman",12,"bold",),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=5)

        update_button=Button(Search_frame,text="Show all",width=14,font=("times new roman",12,"bold",),bg="blue",fg="white")
        update_button.grid(row=0,column=4)

        #***************************Table Frame******************************


        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=0,y=55,width=665,height=420) 

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100) 
        self.student_table.column("photo",width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #*******************Function Declaration******

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Suraj28012000*",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_teacher.get(),
                                                                                                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
            #=============fetch data==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Suraj28012000*",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        #+++++++++++++++++get cursor++++++++++++++++++++

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

    # update function

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Suraj28012000*",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                                                     ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success","Student successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()           
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    


    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","StudentId must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Suraj28012000*",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    # =============================Generate data set or Take photo Samples================================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Suraj28012000*",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                    #=================== Load predefined data on face frontal from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                #cap=cv2.imread(r"F:\attendance_system_using_face_recognition\chetana.jpeg")
                #suraj
                address="http://192.168.43.61:8080/video"
                #chetana
                #address="http://25.152.23.48:8080/video"
                #prajkta
                #address="http://192.168.43.209:8080/video"

                cap.open(address)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="DATA/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def search_data(self):
        if self.serchTxt_var.get()=="" or self.serch_var.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Suraj28012000*",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

            
        



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()