import tkinter as tk
import tkinter.messagebox
from tkinter import *
from CsvUploader import CsvUpload

class AdminDashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.destroy()

        global sup
        sup = Tk()
        self.CsvUploader = CsvUpload

        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Admin Dashboard", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

        log = Button(sup_frame, text='Log out', padx=5, pady=5, width=5, bg="white",
                     fg='blue', underline=1)
        log.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
        log.place(relx=0.4, rely=0.9)

        buttonViewStudentMarks = Button(sup_frame, text="View Student Marks", fg='black', bg='white')
        buttonViewStudentMarks.place(relx=0.31, rely=0.4)
        buttonViewStudentMarks.config(width=30)

        buttonViewStudentMarks = Button(sup_frame, text="Enroll Student To Exam", fg='black', bg='white')
        buttonViewStudentMarks.place(relx=0.31, rely=0.5)
        buttonViewStudentMarks.config(width=30)

        uploadQuestions = Button(sup_frame, text="Upload Questions", fg='black', bg='white',command=self.csvUpload)
        uploadQuestions.place(relx=0.31, rely=0.6)
        uploadQuestions.config(width=30)

        provistionDatabase = Button(sup_frame, text="Provision Database", fg='black', bg='white')
        provistionDatabase.place(relx=0.31, rely=0.7)
        provistionDatabase.config(width=30)

        sup.mainloop()

    def csvUpload(self):
        self.CsvUploader()