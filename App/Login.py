import tkinter as tk
from tkinter import *
from AdminDashboard import AdminDashboard

class LoginPage:
    def __init__(self):

        self.root = tk.Tk()
        self.AdminDashboard = AdminDashboard

        global sup
        sup = Tk()
        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Registration Page", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

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
        sp = Button(sup_frame, text='Log In', padx=5, pady=5, width=5,  bg='green', command=self.LoginClick)
        sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.35, rely=0.8)


        self.root.mainloop()

    def LoginClick(self):
        self.AdminDashboard()