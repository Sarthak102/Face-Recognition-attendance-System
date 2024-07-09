from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Student_details:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x800+0+0")
        self.root.title("Student Details")
        self.root.config(bg="blue")
        # Create the main window
        # window = Tk()
        # window.title("Face Attendance Recognition System")
        # window.geometry("1280x800")

        # Configure the grid layout manager
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)


        #  ======================== Variables ========================
        self.var_std_id = StringVar()
        self.var_seat = StringVar()
        self.var_prn = StringVar()
        self.var_name = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_course = StringVar()
        self.var_dep = StringVar()
        self.var_div = StringVar()
        self.var_email = StringVar()
        self.var_t_name = StringVar()
        

        # Create a Blank white Header Frame
        header_frame=Frame(bd=2,bg="white")
        header_frame.place(x=0,y=0,width=1280,height=55)
        

        # Create the heading label
        title_lbl=Label(header_frame, text="FACE ATTENDANCE RECOGNITION SYSTEM", font=("times new roman", 27, "bold"), bg="white",fg="black")
        title_lbl.place(x=0, y=0, width=1280, height=55)







        # Create the side menu frame
        side_menu_frame = Frame(bg="blue", width=300, height=700)
        side_menu_frame.grid(column=0, row=1, sticky="nsew")
        side_menu_frame.place(x=0, y=55, width=250, height=700)

        # Create the side menu buttons
        button_style = ttk.Style()
        button_style.configure("SideMenu.TButton", font=("Arial", 14), background="#ffffff", foreground="black")

        student_details_button = ttk.Button(side_menu_frame, text="STUDENT DETAILS", style="SideMenu.TButton")
        student_details_button.grid(padx=20, pady=20, sticky="ew")

        face_recognition_button = ttk.Button(side_menu_frame, text="FACE RECOGNITION", style="SideMenu.TButton", command= self.face_recognition)
        face_recognition_button.grid(padx=20, pady=20, sticky="ew")

        attendance_button = ttk.Button(side_menu_frame, text="ATTENDANCE", style="SideMenu.TButton", command=self.attendance )
        attendance_button.grid(padx=20, pady=20, sticky="ew")

        train_data_button = ttk.Button(side_menu_frame, text="TRAIN DATA", style="SideMenu.TButton", command=self.train_classifier )
        train_data_button.grid(padx=20, pady=20, sticky="ew")

        photos_button = ttk.Button(side_menu_frame, text="PHOTOS", style="SideMenu.TButton", command=self.open_img )
        photos_button.grid(padx=20, pady=20, sticky="ew")


        # Create the main content frame
        content_frame = Frame( bg="#9B59B6", height=700)
        content_frame.grid(column=1, row=1, sticky="nsew")

        # Student_Details label
        Student_Details_lbl = Label(text="Student Details", font=("times new roman", 28, "bold"), fg="black", bg="white")
        Student_Details_lbl.place(x=256.5, y=60, width=1017, height=55)


        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=257,y=113,width=1017,height=610)

         #left label frame

        Left_frame=LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=0,y=0,width=420,height=600)

        #Current course

        current_course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        current_course.place(x=4,y=1,width=408,height=130)

        # Department
        dep_label=Label(current_course,text="Department: ", font=("times new roman",10,"bold"), bg="white")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course, textvariable=self.var_dep ,font=("times new roman",9,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer Science","Civil","Mechanical", "ENTC", "AIML" )
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label=Label(current_course,text="Course: ",font=("times new roman",10,"bold"), bg="white")
        course_label.grid(row=0,column=2)

        course_combo=ttk.Combobox(current_course, textvariable= self.var_course ,font=("times new roman",9,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course", "B-Tech", "M-Tech" )
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label=Label(current_course,text="Year: ",font=("times new roman",10,"bold"), bg="white")
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(current_course, textvariable=self.var_year ,font=("times new roman",9,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year", "2020", "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label=Label(current_course,text="Semester: ",font=("times new roman",10,"bold"), bg="white")
        semester_label.grid(row=1,column=2)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_sem,font=("times new roman",9,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)


        # Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=4,y=135,width=408,height=435)

        # Student Id
        std_id_label=Label(class_student_frame,text="Student Id: ",font=("times new roman",10,"bold"), bg="white")
        std_id_label.grid(row=0,column=0, sticky=W)

        std_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id ,width=20, font=("times new roman",10,"bold"))
        std_id_entry.grid(row=0,column=1, padx=2, pady=10, sticky=W)

        # Seat No
        seatno_label=Label(class_student_frame,text="Seat no: ",font=("times new roman",10,"bold"), bg="white")
        seatno_label.grid(row=1,column=0, sticky=W)

        seatno_entry=ttk.Entry(class_student_frame,textvariable=self.var_seat ,width=20, font=("times new roman",10,"bold"))
        seatno_entry.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        # Student Name
        studentName_label=Label(class_student_frame,text="Student Name: ",font=("times new roman",10,"bold"), bg="white")
        studentName_label.grid(row=2,column=0, sticky=W)

        studentName_entry=ttk.Entry(class_student_frame, textvariable=self.var_name ,width=20, font=("times new roman",10,"bold"))
        studentName_entry.grid(row=2,column=1, padx=2, pady=10, sticky=W)

        #Division
        div_label=Label(class_student_frame,text="Division: ",font=("times new roman",10,"bold"), bg="white")
        div_label.grid(row=3,column=0, sticky=W)

        div_entry=ttk.Entry(class_student_frame, textvariable=self.var_div ,width=20, font=("times new roman",10,"bold"))
        div_entry.grid(row=3,column=1, padx=2, pady=10, sticky=W)

        # PRN
        prn_label=Label(class_student_frame,text="PRN: ",font=("times new roman",10,"bold"), bg="white")
        prn_label.grid(row=4,column=0, sticky=W)

        prn_entry=ttk.Entry(class_student_frame,width=20, textvariable=self.var_prn , font=("times new roman",10,"bold"))
        prn_entry.grid(row=4,column=1, padx=2, pady=10, sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email: ",font=("times new roman",10,"bold"), bg="white")
        email_label.grid(row=5,column=0, sticky=W)

        email_entry=ttk.Entry(class_student_frame, textvariable=self.var_email , width=20, font=("times new roman",10,"bold"))
        email_entry.grid(row=5,column=1, padx=2, pady=10, sticky=W)

        # Teacher Name
        teacherName_label=Label(class_student_frame,text="Teacher Name: ",font=("times new roman",10,"bold"), bg="white")
        teacherName_label.grid(row=6,column=0, sticky=W)    

        teacherName_entry=ttk.Entry(class_student_frame, textvariable=self.var_t_name ,width=20, font=("times new roman",10,"bold"))
        teacherName_entry.grid(row=6,column=1, padx=2, pady=10, sticky=W)
        

        # Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1 ,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=7,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame, variable=self.var_radio1 ,text="No Photo Sample",value="No")
        radiobtn2.grid(row=7,column=1)

        # button frame 
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=340,width=408,height=35)

        save_button=Button(btn_frame,text="Save", command=self.add_data , font=("times new roman",10,"bold"), bg="blue", fg="white", width=13)
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Update", command=self.update_data ,font=("times new roman",10,"bold"), bg="blue", fg="white", width=13)
        update_button.grid(row=0,column=1)

        delete_button=Button(btn_frame,text="Delete",command= self.delete_data , font=("times new roman",10,"bold"), bg="blue", fg="white", width=13)
        delete_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",command=self.reset_data , font=("times new roman",10,"bold"), bg="blue", fg="white", width=13)
        reset_button.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=375,width=408,height=35)
        take_photo_button=Button(btn_frame1,text="Take Photo Sample", command=self.generate_dataset , font=("times new roman",10,"bold"), bg="blue", fg="white", width=28)
        take_photo_button.grid(row=0,column=0)

        update_photo_button=Button(btn_frame1,text="Update Photo Sample", command=self.update_dataset, font=("times new roman",10,"bold"), bg="blue", fg="white", width=28)
        update_photo_button.grid(row=0,column=1)
        

        

        #Right label frame

        Right_frame=LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=430,y=0,width=577,height=600)


        # Search system
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=5,width=563,height=110)

        Search_label=Label(Search_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="white",fg="black")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=17)
        Search_combo["values"]=("Select","Seat No.","PRN")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        search_entry=ttk.Entry(Search_frame,font=("times new roman",12,"bold"),width=30)
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        # Search Button Frame

        searchbtn_frame=Frame(Search_frame,relief=RIDGE,bg="white")
        searchbtn_frame.place(x=0,y=50,width=558,height=35)

        # Button
        search_btn=Button(searchbtn_frame,text="Search",width=30,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=0)

        showAll_btn=Button(searchbtn_frame,text="Show All",width=30,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=1,padx=4)


        #Table Frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=120,width=563,height=445)


        #scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("std_id" ,"seat","prn","name","year", "sem", "course", "dep", "div", "email", "t_name", "photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("std_id",text="Student Id")
        self.student_table.heading("seat",text="Seat No.")
        self.student_table.heading("prn",text="PRN")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("t_name",text="Teacher Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("std_id",width=100)
        self.student_table.column("seat",width=100)
        self.student_table.column("prn",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("t_name",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()




    # =================================== FUNCTION DECLARATION ===================================
    
    def add_data(self):
        if self.var_dep.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_sem.get()=="" or self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_seat.get()=="" or self.var_prn.get()=="" or self.var_name.get()=="" or self.var_div.get()=="" or self.var_email.get()=="" or self.var_t_name.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_attendence")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student (std_id, seat, prn, name, year, sem, course, dep, `div`, email, t_name, photo_sample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                                                self.var_std_id.get(),
                                                                                                                                                self.var_seat.get(),
                                                                                                                                                self.var_prn.get(),
                                                                                                                                                self.var_name.get(),
                                                                                                                                                self.var_year.get(),
                                                                                                                                                self.var_sem.get(),
                                                                                                                                                self.var_course.get(),
                                                                                                                                                self.var_dep.get(),
                                                                                                                                                self.var_div.get(),
                                                                                                                                                self.var_email.get(),
                                                                                                                                                self.var_t_name.get(),
                                                                                                                                                self.var_radio1.get()
                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)
        
        


    #  ======================== Fetch Data ========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_attendence")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    # ======================== get cursor ========================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0])
        self.var_seat.set(data[1])
        self.var_prn.set(data[2])
        self.var_name.set(data[3])
        self.var_year.set(data[4])
        self.var_sem.set(data[5])
        self.var_course.set(data[6])
        self.var_dep.set(data[7])
        self.var_div.set(data[8])
        self.var_email.set(data[9])
        self.var_t_name.set(data[10])
        self.var_radio1.set(data[11])


    # ======================== Update Function ========================
    def update_data(self):
        if self.var_dep.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_sem.get()=="" or self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_seat.get()=="" or self.var_prn.get()=="" or self.var_name.get()=="" or self.var_div.get()=="" or self.var_email.get()=="" or self.var_t_name.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                   conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_attendence")
                   print("Database connected successfully")  # Debug line

                   my_cursor = conn.cursor()
                   sql_query = "update student set seat=%s, prn=%s, `name`=%s, year=%s, sem=%s, course=%s, dep=%s, `div`=%s, email=%s, t_name=%s, photo_sample=%s where std_id=%s"
                   data = (
                        self.var_seat.get(),
                        self.var_prn.get(),
                        self.var_name.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_course.get(),
                        self.var_dep.get(),
                        self.var_div.get(),
                        self.var_email.get(),
                        self.var_t_name.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )
                   print(f"Executing query: {sql_query} with data: {data}")  # Debug line
                   my_cursor.execute(sql_query, data)
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)
        
    # ======================== Delete Function ========================
    def delete_data(self):
        if self.var_seat.get() == "":
            messagebox.showerror("Error", "Seat number must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Details", "Do you want to delete this student details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_attendence")
                    my_cursor = conn.cursor()
                    sql_query = "delete from student where std_id=%s"
                    data = (self.var_std_id.get(),)
                    my_cursor.execute(sql_query, data)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    # ======================== Reset Function ========================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_seat.set("")
        self.var_prn.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_email.set("")
        self.var_t_name.set("")
        self.var_radio1.set("")

        self.fetch_data()

    # ======================== Generate Dataset ========================
    def generate_dataset(self):
        if self.var_dep.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_sem.get()=="" or self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_seat.get()=="" or self.var_prn.get()=="" or self.var_name.get()=="" or self.var_div.get()=="" or self.var_email.get()=="" or self.var_t_name.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_attendence")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                sql_query = "update student set seat=%s, prn=%s, `name`=%s, year=%s, sem=%s, course=%s, dep=%s, `div`=%s, email=%s, t_name=%s, photo_sample=%s where std_id=%s"
                data = (
                    self.var_seat.get(),
                    self.var_prn.get(),
                    self.var_name.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_course.get(),
                    self.var_dep.get(),
                    self.var_div.get(),
                    self.var_email.get(),
                    self.var_t_name.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                )
                print(f"Executing query: {sql_query} with data: {data}")  # Debug line
                my_cursor.execute(sql_query, data)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ======================== Load prerdained data on face frontals from opencv ========================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minimum neighbour = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


    # ======================== Update Dataset ========================
    def update_dataset(self):
        if self.var_dep.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_sem.get()=="" or self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_seat.get()=="" or self.var_prn.get()=="" or self.var_name.get()=="" or self.var_div.get()=="" or self.var_email.get()=="" or self.var_t_name.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_attendence")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                sql_query = "update student set seat=%s, prn=%s, `name`=%s, year=%s, sem=%s, course=%s, dep=%s, `div`=%s, email=%s, t_name=%s, photo_sample=%s where std_id=%s"
                data = (
                    self.var_seat.get(),
                    self.var_prn.get(),
                    self.var_name.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_course.get(),
                    self.var_dep.get(),
                    self.var_div.get(),
                    self.var_email.get(),
                    self.var_t_name.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                )
                print(f"Executing query: {sql_query} with data: {data}")  # Debug line
                my_cursor.execute(sql_query, data)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ======================== Load prerdained data on face frontals from opencv ========================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minimum neighbour = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset updated successfully!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    

    # ============================================ Other Pages ============================================
    # ======================== Open Photo ========================
    def open_img(self):
        os.startfile("data")
    
    # ======================== Train Classifier ========================
    def train_classifier(self):
        # Create a confirmation dialog box
        confirmation = messagebox.askyesno("Confirmation", "Do you want to train the classifier?")

        # Check user's choice
        if confirmation:
            data_dir = "data"
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            faces = []
            ids = []

            for image in path:
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1) == 13

            ids = np.array(ids)

            # Train the classifier and save the model into classifier.xml
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training dataset completed!!!")

    


    # ======================== Attendence ========================
    def mark_attendance(self, std_id, seat, name):
        with open("attendence.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((std_id not in name_list) and (seat not in name_list) and (name not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{std_id},{seat},{name},{dtString},{d1},Present")

    # ======================== Face Recognition ========================
    def face_recognition(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
                id, pred = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100*(1-pred/300))

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_attendence")
                my_cursor = conn.cursor()
                my_cursor.execute("select `name` from student where std_id="+str(id))
                name = my_cursor.fetchone()
                name = "".join(name)

                my_cursor.execute("select `seat` from student where std_id="+str(id))
                seat = my_cursor.fetchone()
                seat = "".join(seat)
                
                my_cursor.execute("select `std_id` from student where std_id="+str(id))
                std_id = my_cursor.fetchone()
                std_id = "".join(std_id)

                if confidence > 77:
                    cv2.putText(img, f"Student Id: {std_id}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name: {name}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Seat: {seat}", (x, y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(std_id, seat, name)
                    # cv2.putText(img, f"Confidence: {confidence}", (x, y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                
                coord = [x, y, w, h]
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Camera Closed")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                # break
                cv2.destroyAllWindows()
                video_cap.release()
            # video_cap.release()
            # cv2.destroyAllWindows()
    
    # ======================== Redirect to attendance ========================
    def attendance(self):
        self.root.destroy()
        os.system("python attendance.py")

    
















if __name__ == "__main__":
    root = Tk()
    obj = Student_details(root)
    root.mainloop()