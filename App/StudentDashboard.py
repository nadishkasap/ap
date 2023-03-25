import tkinter as tk
from tkinter import *
# from Exam import ExamLandingPage
from ExamLandingPage import ExamLandingPage
from Database import Database
import json


class StudentDashboard:
    def __init__(self,rowId,userFirstName,userLastName,userEmail):
        self.ExamLandingPage = ExamLandingPage
        self.database = Database
        self.rowId = rowId
        self.userFirstName = userFirstName
        self.userLastName = userLastName
        self.userEmail = userEmail

        self.userDictionary = {
            "userId": self.rowId,
            "userFirstName": self.userFirstName,
            "userLastName": self.userLastName,
            "userEmail": self.userEmail
        }
        global sup
        sup = Tk()
        sup.attributes('-fullscreen', True)
        sup.title("Student Dashboard - LMS University of Kelaniya")

        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack(fill=tk.BOTH, expand=True)
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Student Dashboard", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

        heading = Label(sup_frame, text="Welcome, " + self.userFirstName, fg="black", bg="white")
        heading.config(font=('calibri 15'))
        heading.place(relx=0.2, rely=0.2)

        # Quite Button
        quit_button = Button(sup_frame, text="X", command=sup.destroy, width=5, bg="black", pady=10, padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        #Student ID
        lblStudentId = Label(sup_frame, text="Student Id : ", fg="black", bg="white")
        lblStudentId.config(font=('calibri 16'))
        lblStudentId.place(relx=0.2, rely=0.3)

        valStudentId = Label(sup_frame, text=self.rowId, fg="black", bg="white")
        valStudentId.config(font=('calibri 16'))
        valStudentId.place(relx=0.5, rely=0.3)
        # Student Name
        lblStudentName = Label(sup_frame, text="Student Name : ", fg="black", bg="white")
        lblStudentName.config(font=('calibri 16'))
        lblStudentName.place(relx=0.2, rely=0.4)

        valStudentName = Label(sup_frame, text= self.userFirstName+" "+self.userLastName , fg="black", bg="white")
        valStudentName.config(font=('calibri 16'))
        valStudentName.place(relx=0.5, rely=0.4)

        # Student Name
        lblStudentMarks= Label(sup_frame, text="Marks : ", fg="black", bg="white")
        lblStudentMarks.config(font=('calibri 16'))
        lblStudentMarks.place(relx=0.2, rely=0.5)

        valStudentMarks = Label(sup_frame, text=" - ", fg="black", bg="white")
        valStudentMarks.config(font=('calibri 16'))
        valStudentMarks.place(relx=0.5, rely=0.5)


 		# Take Exam
        sp = Button(sup_frame, text='Take Exam ->', padx=4, pady=4, width=5,  bg='green',foreground='white',command=self.ExamLandingPage)
        sp.configure(width=30, height=2, activebackground="#33B5E5", relief=FLAT)
        sp.config(font=('calibri 16 bold'))
        sp.place(relx=0.31, rely=0.8)        

        sp.place(relx=0.4, rely=0.7)
        lblSelectExam = Label(sup_frame, text="Select Exam", fg="black", bg="white")
        lblSelectExam.config(font=('calibri 16'))
        lblSelectExam.place(relx=0.2, rely=0.6)

        ExamIds = [
            "FGSMIT2021",
            "FGSMIT2022",
            "FGSMIT2023"
        ]

        #DropDown
        examIDVar = StringVar(sup)
        examIDVar.set(ExamIds[0])  # default value

        OptionList = OptionMenu(sup_frame, examIDVar, *ExamIds)
        OptionList.place(relx=0.5, rely=0.6)

        db = self.database('localhost', 'root', '', 'quiz')
        db.connect()
        cursor = db.connection.cursor()
        examType = 'e1'
        selectQuery = "SELECT * FROM question where examType=%s"
        val = (examType,)
        cursor.execute(selectQuery, val)
        results = cursor.fetchall()
        question = []
        for row in results:
            question.append(row[1])

        answer = []
        for row in results:
            answer.append(row[6])

        options = []
        tempOptions = []
        for row2 in results:
            tempOptions.append(row2[2])
            tempOptions.append(row2[3])
            tempOptions.append(row2[4])
            tempOptions.append(row2[5])

            options.append(tempOptions)
            tempOptions = []

        data = {
            "question": question,
            "answer": answer,
            "options": options
        }
        data2 = json.dumps(data)
        f = open("data.json", "w+")
        f.write(data2)
        f.close()

        sup.mainloop()

    def startExam(self):
        self.ExamLandingPage()
