import os
import tkinter as tk
from tkinter import *
from CsvUploader import CsvUpload
from StudentMarks import StudentMarks
import webbrowser
class AdminDashboard:
    def __init__(self, rowId, userFirstName, userLastName, userEmail):

        self.root = tk.Tk()
        self.root.destroy()

        self.rowId = rowId
        self.userFirstName = userFirstName
        self.userLastName = userLastName
        self.userEmail = userEmail

        print(self.rowId,self.userFirstName,self.userLastName,self.userEmail)

        global sup
        sup = Tk()
        self.CsvUploader = CsvUpload
        self.StudentMarks = StudentMarks

        sup.attributes('-fullscreen', True)
        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack(fill=tk.BOTH, expand=True)
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Admin Dashboard", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

        global  nameVar
        nameVar = StringVar()
        nameVar.set("Welcome, "+self.userFirstName)
        heading = Label(sup_frame, text="Welcome, "+self.userFirstName , fg="black", bg="white")
        heading.config(font=('calibri 15'))
        heading.place(relx=0.2, rely=0.2)

        # Quite Button
        quit_button = Button(sup_canvas, text="X", command=sup.destroy, width=5, bg="black", pady=10, padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        buttonViewStudentMarks = Button(sup_frame, text="View Student Marks", fg='black', bg='white',command=self.studentMarks)
        buttonViewStudentMarks.place(relx=0.31, rely=0.4)
        buttonViewStudentMarks.config(width=30)

        # buttonViewStudentMarks = Button(sup_frame, text="Enroll Student To Exam", fg='black', bg='white')
        # buttonViewStudentMarks.place(relx=0.31, rely=0.5)
        # buttonViewStudentMarks.config(width=30)

        uploadQuestions = Button(sup_frame, text="Upload Questions", fg='black', bg='white',command=self.csvUpload)
        uploadQuestions.place(relx=0.31, rely=0.6)
        uploadQuestions.config(width=30)

        provistionDatabase = Button(sup_frame, text="Download Quiz Template", fg='black', bg='white', command=self.link)
        provistionDatabase.place(relx=0.31, rely=0.7)
        provistionDatabase.config(width=30)

        sup.mainloop()

    def csvUpload(self):
        self.CsvUploader()

    def studentMarks(self):
        self.StudentMarks()

    currentWD = os.getcwd()
    global filepath
    filepath = currentWD+"sample_quiz_template.csv"
    def link(self):
        print("filepath",filepath)
        webbrowser.open_new(filepath)
