import tkinter as tk
import tkinter.messagebox
from tkinter import *

class ExamLandingPage:
    def __init__(self):


        window = tk.Tk()

        # self.root = tk.Tk()
        # self.root.destroy()

        ex_canvas = Canvas(window, width=720, height=440, bg="#600")
        ex_canvas.pack()

        ex_frame = Frame(ex_canvas, bg="white")
        ex_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(ex_frame, text="Ready to take your exam!", fg="brown", bg="white")
        heading.config(font=('calibri 25'))
        heading.place(relx=0.2, rely=0.1)

        self.varMesasgeX = StringVar()
        self.varMesasgeX.set("Welcome to the online exam for [course name]. Please read the following instructions carefully before starting the exam: The exam is timed and will be available for [duration]. You are expected to complete the exam within this time limit.")
        message = Label(ex_frame, bg='white',  textvariable=self.varMesasgeX, wraplength=400)
        message.place(relx=0.15, rely=0.3)

        lblExamDuration = Label(ex_frame, text="Exam Duration: 1h", fg="brown", bg="white")
        lblExamDuration.config(font=('calibri 12'))
        lblExamDuration.place(relx=0.2, rely=0.55)

        lblExamType = Label(ex_frame, text="Exam Type: MCQ", fg="brown", bg="white")
        lblExamType.config(font=('calibri 12'))
        lblExamType.place(relx=0.2, rely=0.65)

        btnStartExam = Button(ex_frame, text="Click me!",)
        # img = PhotoImage(file="D:/SEM 4/AP_Project/ap/App/images/btn-start-exam.png")
        # btnStartExam.config(image=img,pady=10)
        btnStartExam.place(relx=0.31, rely=0.8)


        window.mainloop()
