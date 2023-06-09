import tkinter as tk
from Exam import Exam
from tkinter import *


class ExamLandingPage:
    def __init__(self,rowId,userFirstName,userLastName,userEmail,examIDvar):

        self.rowId = rowId
        self.userFirstName = userFirstName
        self.userLastName = userLastName
        self.userEmail = userEmail
        self.examIDvar = examIDvar

        global window
        self.Exam = Exam
        window = tk.Tk()
        window.attributes('-fullscreen', True)  # make main window full-screen

        ex_canvas = Canvas(window, width=720, height=440, bg="#600")
        ex_canvas.pack(fill=tk.BOTH, expand=True)
        ex_canvas.pack()

        ex_frame = Frame(ex_canvas, bg="white")
        ex_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        # Exam heading
        heading = Label(ex_frame, text=' EXAM: Advanced Programming ', fg="white", bg="#101357", width=60)
        heading.config(font=('Arial 22'))
        heading.place(relx=0.5, rely=.05, anchor=CENTER)
        heading.config(text=self.examIDvar)

        # Quite Button
        quit_button = Button(ex_canvas, text="X", command=window.destroy,  width=5, bg="black", pady=10, padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        para = Label(ex_frame, bg='white',text="Welcome to the online exam for Advance Programming. Please read the following instructions carefully before starting the exam: The exam is timed and will be available for [1 Hour]. You are expected to complete the exam within this time limit.", wraplength=600)
        para.config(font=('Arial 14'))
        para.place(relx=0.5, rely=.3, anchor=CENTER)

        lblExamDuration = Label(ex_frame, text="Exam Duration: 1h", fg="brown", bg="white")
        lblExamDuration.config(font=('calibri 24 bold'))
        lblExamDuration.place(relx=0.2, rely=0.5, anchor=CENTER)

        lblExamType = Label(ex_frame, text="Exam Type: MCQ", fg="brown", bg="white")
        lblExamType.config(font=('calibri 24 bold'))
        lblExamType.place(relx=0.2, rely=0.6, anchor=CENTER)

        btnStartExam = Button(ex_frame, text='Start Exam ->', padx=4, pady=4, width=30, bg='green',fg='white', command=self.goToExam)
        btnStartExam.configure(width=30, height=2, activebackground="#33B5E5", relief=FLAT)
        btnStartExam.config(font=('calibri 16 bold'))
        btnStartExam.place(relx=0.31, rely=0.8)

        window.mainloop()

    def goToExam(self):
        window.destroy()
        self.Exam(self.rowId,self.userFirstName,self.userLastName,self.userEmail,self.examIDvar)

