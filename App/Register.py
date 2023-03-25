import tkinter as tk
from tkinter import *
from Database import Database
from Login import LoginPage


class Register(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.destroy()
        self.database = Database

        self.LoginPage = LoginPage
        global sup

        sup = Tk()
        sup.attributes('-fullscreen', True)  # make main window full-screen

        self.fname = StringVar()
        self.lname = StringVar()
        self.passW = StringVar()
        self.email = StringVar()

        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack(fill=tk.BOTH, expand=True)
        sup_canvas.pack()

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        ###Quite Button
        quit_button = Button(sup_frame, text="X", command=sup.destroy, width=5, bg="black", pady=10,
                             padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        heading = Label(sup_frame, text="Registration Page", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)

        # firstname
        flabel = Label(sup_frame, text="First Name", fg='black', bg='white',font=('Georgia 16'))
        flabel.place(relx=0.21, rely=0.3)
        self.fname = Entry(sup_frame, bg='#d3d3d3',  fg='#560600', textvariable=self.fname,font=('Georgia 16'))
        self.fname.config(width=30, border=1, bg="#F7FBFF")
        self.fname.place(relx=0.32, rely=0.3)

        # lastname
        ulabel = Label(sup_frame, text="Last Name", fg='black', bg='white',font=('Georgia 16'))
        ulabel.place(relx=0.21, rely=0.4)
        self.lname = Entry(sup_frame, bg='#d3d3d3',  fg='#560600', textvariable=self.lname,font=('Georgia 16'))
        self.lname.config(width=30, border=1, bg="#F7FBFF")
        self.lname.place(relx=0.32, rely=0.4)

        # email
        clabel = Label(sup_frame, text="Email", fg='black', bg='white',font=('Georgia 16'))
        clabel.place(relx=0.215, rely=0.5)
        self.email = Entry(sup_frame, bg='#d3d3d3',  fg='#560600', textvariable=self.email,font=('Georgia 16'))
        self.email.config(width=30, border=1, bg="#F7FBFF")
        self.email.place(relx=0.32, rely=0.5)

        # password
        plabel = Label(sup_frame, text="Password", fg='black', bg='white',font=('Georgia 16'))
        plabel.place(relx=0.215, rely=0.6)
        self.passW = Entry(sup_frame, bg='#d3d3d3',  fg='#560600', show="*", textvariable=self.passW,font=('Georgia 16'))
        self.passW.config(width=30, border=1, bg="#F7FBFF")
        self.passW.place(relx=0.32, rely=0.6)

        global errVar
        errVar = StringVar(sup)
        errMessage = Label(sup_frame, textvariable=errVar, fg="red", bg="white")
        errMessage.config(font=('calibri 12 bold'))
        errMessage.place(relx=0.21, rely=0.7)

        # signup BUTTON
        sp = Button(sup_frame, text='Register ', fg="white", padx=5, pady=5, width=5, bg='green', command=self.signUp,font=('Georgia 14'))
        sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.4, rely=0.8)

        log = Button(sup_frame, text='Already have a Account? login here', padx=5, pady=5, width=5, bg="white",
                     fg='blue' ,command=LoginPage)
        log.configure(width=25, height=1, activebackground="#33B5E5", relief=FLAT)
        log.place(relx=0.4, rely=0.9)

        self.root.mainloop()

    def register(self):
        self.LoginPage()

    def signUp(self):
        fname = self.fname.get()
        lname = self.lname.get()
        passW = self.passW.get()
        email = self.email.get()

        if fname == '' or lname =='' or passW == '' or email == '':
            errVar.set("Please fill all the fields!")
        else:

            try:
                db = self.database('localhost', 'root', '', 'quiz')
                conn =db.connect()
                cursor = db.connection.cursor()
                insertQuery = """INSERT INTO user (fname, lname, email,passW,userType) VALUES (%s, %s, %s,%s,%s)"""
                val = (fname, lname, email, passW, 2)
                cursor.execute(insertQuery, val)
                db.connection.commit()
                self.LoginPage()

            except TypeError as e:
                errVar.set(e)
                print(e)
                return None
