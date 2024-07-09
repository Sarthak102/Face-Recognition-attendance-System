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
import csv
from tkinter import filedialog
from index import Student_details


mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x800+0+0")
        self.root.title("Attendance System")
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
        self.var_name = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance_status = StringVar()
        

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

        student_details_button = ttk.Button(side_menu_frame, text="STUDENT DETAILS", style="SideMenu.TButton", command=self.redirect)
        student_details_button.grid(padx=20, pady=20, sticky="ew")

        face_recognition_button = ttk.Button(side_menu_frame, text="FACE RECOGNITION", style="SideMenu.TButton", command= self.face_recognition)
        face_recognition_button.grid(padx=20, pady=20, sticky="ew")

        attendance_button = ttk.Button(side_menu_frame, text="ATTENDANCE", style="SideMenu.TButton")
        attendance_button.grid(padx=20, pady=20, sticky="ew")

        train_data_button = ttk.Button(side_menu_frame, text="TRAIN DATA", style="SideMenu.TButton", command=self.train_classifier )
        train_data_button.grid(padx=20, pady=20, sticky="ew")

        photos_button = ttk.Button(side_menu_frame, text="PHOTOS", style="SideMenu.TButton", command=self.open_img )
        photos_button.grid(padx=20, pady=20, sticky="ew")


        # Create the main content frame
        content_frame = Frame( bg="#9B59B6", height=700)
        content_frame.grid(column=1, row=1, sticky="nsew")

        # Attendance label
        Attandace_lbl = Label(text="Attendance", font=("times new roman", 28, "bold"), fg="black", bg="white")
        Attandace_lbl.place(x=256.5, y=60, width=1017, height=55)


        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=257,y=113,width=1017,height=610)


        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=500,height=590)

        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=515,y=10,width=495,height=590)

        #  ======================== Left Frame ========================
        # Student ID
        std_id_lbl=Label(Left_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        std_id_lbl.grid(row=0,column=0,padx=20,pady=15,sticky="w")

        std_id_entry=ttk.Entry(Left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        std_id_entry.grid(row=0,column=1,padx=20,pady=15,sticky="w")

        # Seat
        seat_lbl=Label(Left_frame,text="Seat",font=("times new roman",12,"bold"),bg="white")
        seat_lbl.grid(row=1,column=0,padx=20,pady=15,sticky="w")

        seat_entry=ttk.Entry(Left_frame,textvariable=self.var_seat,width=20,font=("times new roman",12,"bold"))
        seat_entry.grid(row=1,column=1,padx=20,pady=15,sticky="w")

        # Name
        name_lbl=Label(Left_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        name_lbl.grid(row=2,column=0,padx=20,pady=15,sticky="w")

        name_entry=ttk.Entry(Left_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=2,column=1,padx=20,pady=15,sticky="w")

        # Time
        time_lbl=Label(Left_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_lbl.grid(row=3,column=0,padx=20,pady=15,sticky="w")

        time_entry=ttk.Entry(Left_frame,textvariable=self.var_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=3,column=1,padx=20,pady=15,sticky="w")

        # Date
        date_lbl=Label(Left_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_lbl.grid(row=4,column=0,padx=20,pady=15,sticky="w")

        date_entry=ttk.Entry(Left_frame,textvariable=self.var_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=4,column=1,padx=20,pady=15,sticky="w")

        # Attendance Status dropdown
        attendance_status_lbl=Label(Left_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        attendance_status_lbl.grid(row=5,column=0,padx=20,pady=15,sticky="w")

        attendance_status_combo=ttk.Combobox(Left_frame,textvariable=self.var_attendance_status,font=("times new roman",12,"bold"),width=18,state="readonly")
        attendance_status_combo["values"]=("Status","Present","Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=5,column=1,padx=20,pady=15,sticky="w")

        # Button Frame
        btn_frame=Frame(Left_frame, relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=400,width=490,height=100)

        # import csv button
        import_btn=Button(btn_frame,text="Import CSV", command=self.importCsv,width=23,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0,padx=10,pady=10)

        # export csv button
        export_btn=Button(btn_frame,text="Export CSV", command=self.exportCsv ,width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1,padx=10,pady=10)

        # update button
        update_btn=Button(btn_frame,text="Update",width=23,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=0,padx=10,pady=10)

        # reset button
        reset_btn=Button(btn_frame,text="Reset",width=24,command=self.reset_data ,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=1,padx=10,pady=10)

        #  ======================== Right Frame ========================
        # table frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=480,height=550)

        # scroll bar
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("std_id","seat","name","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("std_id",text="Student ID")
        self.AttendanceReportTable.heading("seat",text="Seat")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("std_id",width=100)
        self.AttendanceReportTable.column("seat",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # =================== fetch data =================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
        
    # =================== Import Csv =================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # =================== Export Csv =================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                csvwrite=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # =================== Get Cursor =================
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content["values"]
        self.var_std_id.set(row[0])
        self.var_seat.set(row[1])
        self.var_name.set(row[2])
        self.var_time.set(row[3])
        self.var_date.set(row[4])
        self.var_attendance_status.set(row[5])

    # =================== Reset =================
    def reset_data(self):
        self.var_std_id.set("")
        self.var_seat.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("")













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

    # ======================== Redirect to index ========================
    def redirect(self):
        self.root.destroy()
        root = Tk()
        obj = Student_details(root)
        root.mainloop()

        







if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()