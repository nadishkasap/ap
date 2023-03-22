import tkinter as tk
from tkinter import *
from Login import LoginPage

class Register:
    def __init__(self):
        self.root = tk.Tk()
        self.root.destroy()
        global sup
        sup = Tk()

        fname = StringVar()
        uname = StringVar()
        passW = StringVar()
        country = StringVar()

        sup_canvas = Canvas(sup, width=720, height=440, bg="blue")
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Registration Page", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

        # firstname
        flabel = Label(sup_frame, text="First Name", fg='black', bg='white')
        flabel.place(relx=0.21, rely=0.4)
        fname = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=fname)
        fname.config(width=42)
        fname.place(relx=0.31, rely=0.4)

        # lastname
        ulabel = Label(sup_frame, text="Last Name", fg='black', bg='white')
        ulabel.place(relx=0.21, rely=0.5)
        user = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=uname)
        user.config(width=42)
        user.place(relx=0.31, rely=0.5)

        # email
        clabel = Label(sup_frame, text="Email", fg='black', bg='white')
        clabel.place(relx=0.215, rely=0.6)
        c = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=country)
        c.config(width=42)
        c.place(relx=0.31, rely=0.6)

        # password
        plabel = Label(sup_frame, text="Password", fg='black', bg='white')
        plabel.place(relx=0.215, rely=0.7)
        pas = Entry(sup_frame, bg='#d3d3d3', fg='black', show="*", textvariable=passW)
        pas.config(width=42)
        pas.place(relx=0.31, rely=0.7)

        self.root.mainloop()

    def register(self):
        self.LoginPage()
