import tkinter as tk
from tkinter import *
from AdminDashboard import AdminDashboard
from StudentDashboard import  StudentDashboard

class LoginPage:
    def __init__(self):

        self.AdminDashboard = AdminDashboard
        self.StudentDashboard = StudentDashboard
        global sup

        sup = Tk()

        sup.attributes('-fullscreen', True)  # make main window full-screen
        sup.title("Login - LMS University of Kelaniya")
        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack(fill=tk.BOTH, expand=True)
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Login Page", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

        #Quite Button
        quit_button = Button(sup_frame, text="X", command=sup.destroy,
                             width=5, bg="black", pady=10, padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        # Username
        flabel = Label(sup_frame, text="User Name", fg='black', bg='white')
        flabel.place(relx=0.21, rely=0.4)
        fname = Entry(sup_frame, bg='#d3d3d3', fg='black')
        fname.config(width=42)
        fname.place(relx=0.32, rely=0.4)

        # Password
        ulabel = Label(sup_frame, text="Password", fg='black', bg='white')
        ulabel.place(relx=0.21, rely=0.5)
        user = Entry(sup_frame, bg='#d3d3d3', fg='black')
        user.config(width=42)
        user.place(relx=0.32, rely=0.5)

        # Login BUTTON
        sp = Button(sup_frame, text='Log In - ADMIN', padx=5, pady=5, width=5,  bg='green', command=self.LoginClick)
        sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.35, rely=0.7)

        # Login BUTTON TEMPORARY
        sp = Button(sup_frame, text='Log In TEMP - Student', padx=5, pady=5, width=5, bg='green', command=self.TemFuncClick)
        sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.35, rely=.8)


        sup.mainloop()

    def LoginClick(self):
        self.AdminDashboard()

    def TemFuncClick(self):
        self.StudentDashboard()
