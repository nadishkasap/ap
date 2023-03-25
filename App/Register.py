import tkinter as tk
from tkinter import *
from Database import Database


class Register(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.destroy()
        self.database = Database
        global sup
        sup = Tk()

        self.fname = StringVar()
        self.lname = StringVar()
        self.passW = StringVar()
        self.email = StringVar()

        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Registration Page", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

        # firstname
        flabel = Label(sup_frame, text="First Name", fg='black', bg='white')
        flabel.place(relx=0.21, rely=0.4)
        self.fname = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=self.fname)
        self.fname.config(width=42)
        self.fname.place(relx=0.32, rely=0.4)

        # lastname
        ulabel = Label(sup_frame, text="Last Name", fg='black', bg='white')
        ulabel.place(relx=0.21, rely=0.5)
        self.lname = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=self.lname)
        self.lname.config(width=42)
        self.lname.place(relx=0.32, rely=0.5)

        # email
        clabel = Label(sup_frame, text="Email", fg='black', bg='white')
        clabel.place(relx=0.215, rely=0.6)
        self.email = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=self.email)
        self.email.config(width=42)
        self.email.place(relx=0.32, rely=0.6)

        # password
        plabel = Label(sup_frame, text="Password", fg='black', bg='white')
        plabel.place(relx=0.215, rely=0.7)
        self.passW = Entry(sup_frame, bg='#d3d3d3', fg='black', show="*", textvariable=self.passW)
        self.passW.config(width=42)
        self.passW.place(relx=0.32, rely=0.7)

        # signup BUTTON
        sp = Button(sup_frame, text='SignUp', padx=5, pady=5, width=5, bg='green', command=self.signUp)
        sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.4, rely=0.8)

        log = Button(sup_frame, text='Already have a Account?', padx=5, pady=5, width=5, bg="white",
                     fg='blue')
        log.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
        log.place(relx=0.4, rely=0.9)

        self.root.mainloop()

    def register(self):
        self.LoginPage()

    def signUp(self):
        fname = self.fname.get()
        lname = self.lname.get()
        email = self.email.get()

        db = self.database('localhost', 'root', '', 'quiz')
        db.connect()
        cursor = db.connection.cursor()
        insertQuery = """INSERT INTO user (fname, lname, email,user_type) VALUES (%s, %s, %s,%s)"""
        val = (fname, lname, email,2)
        cursor.execute(insertQuery, val)
        db.connection.commit()
