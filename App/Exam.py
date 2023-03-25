import tkinter as tk
from tkinter import *
from Login import LoginPage

class Exam:
    def __init__(self):

        global sup

        sup = Tk()
        sup.attributes('-fullscreen', True)  # make main window full-screen
        sup.title(" Exam - LMS University of Kelaniya")

        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack(fill=tk.BOTH, expand=True)
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Exam: ", fg="black", bg="white")
        heading.config(font=('calibri 20'))
        heading.place(relx=0.1, rely=0.04)

        headingValue = Label(sup_frame, text="Advanced Programming", fg="black", bg="white")
        headingValue.config(font=('calibri 20'))
        headingValue.place(relx=0.2, rely=0.04)

        quiz_frame = Frame(sup_canvas, bg="#DBE4C6")
        quiz_frame.place(relwidth=0.5, relheight=0.5, relx=0.24, rely=0.2)

        # signup BUTTON
        sp = Button(sup_frame, text='Finish Exam', padx=5, pady=5, width=5,  bg='green')
        sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.4, rely=0.95)

        # signup BUTTON
        sp = Button(sup_frame, text='Exit Exam', padx=5, pady=5, width=5, bg='red', command=sup.destroy )
        sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.6, rely=0.85)


        sup.mainloop()

    def register(self):
        self.LoginPage()

Exam()