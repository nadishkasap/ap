import tkinter as tk
import tkinter.messagebox
from tkinter import *

class ExamLandingPage:
    def __init__(self):
        global sup
        sup = Tk()

        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Ready to take your exam!", fg="brown", bg="white")
        heading.config(font=('calibri 25'))
        heading.place(relx=0.2, rely=0.1)

        

        btnStartExam = Button(sup_frame, text="Click me!",)
        img = PhotoImage(file="D:/SEM 4/AP_Project/ap/App/images/btn-start-exam.png")
        btnStartExam.config(image=img,pady=10)
        btnStartExam.place(relx=0.31, rely=0.7)


        sup.mainloop()

ExamLandingPage()