import tkinter as tk
from tkinter import *
from AdminDashboard import AdminDashboard
from StudentDashboard import StudentDashboard
from Database import Database

class LoginPage:
    def __init__(self):

        self.AdminDashboard = AdminDashboard
        self.StudentDashboard = StudentDashboard
        global sup

        sup = Tk()
        self.database = Database
        self.fname = StringVar()
        self.passW = StringVar()

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
        quit_button = Button(sup, text="X", command=sup.destroy, width=5, bg="black", pady=10, padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        # Username
        flabel = Label(sup_frame, text="User Name", fg='black', bg='white',font=('Georgia 16'))
        flabel.place(relx=0.21, rely=0.4)
        self.fname = Entry(sup_frame,  fg='#560600',textvariable=self.fname, font=('Georgia 16'))
        self.fname.config(width=30,border=1,bg="#F7FBFF")
        self.fname.place(relx=0.32, rely=0.4)

        # Password
        ulabel = Label(sup_frame, text="Password", fg='black', bg='white',font=('Georgia 16'))
        ulabel.place(relx=0.21, rely=0.5)
        self.passW = Entry(sup_frame,  fg='#560600',textvariable=self.passW, font=('Georgia 16'))
        self.passW.config(width=30,border=1,bg="#F7FBFF")
        self.passW.place(relx=0.32, rely=0.5)

        global errVar
        errVar = StringVar()
        errMessage = Label(sup_frame, textvariable=errVar, fg="red", bg="white")
        errMessage.config(font=('calibri 12 bold'))
        errMessage.place(relx=0.21, rely=0.6)

        # Login BUTTON
        sp = Button(sup_frame, text='Log in', padx=1, pady=1, width=5,  bg='green', command=self.LoginClick)
        sp.configure(width=20, height=2, activebackground="#33B5E5", relief=FLAT)
        sp.config(font=('calibri 14 bold'))
        sp.place(relx=0.32, rely=0.7)

        sup.mainloop()

    def LoginClick(self):

        fname = self.fname.get()
        passW = self.passW.get()
        print(fname, " | ", passW)
        db = self.database('localhost', 'root', '', 'quiz')
        db.connect()

        cursor = db.connection.cursor()
        selectQuery = """SELECT * FROM user where fname=%s and passW=%s"""
        val = (fname, passW)
        cursor.execute(selectQuery, val)
        results = cursor.fetchall()

        print(results)
        if len(results) < 1:
            errVar.set("Invalid Username or Password! Try Again.")
        else:
            for i in results: # check if admin or student
                rowId = i[0]
                userFirstName = i[1]
                userLastName = i[2]
                userEmail = i[3]

                if i[5] == 1: # Check usertype == admin (1)
                    self.AdminDashboard(rowId,userFirstName,userLastName,userEmail)
                elif i[5] ==2: # Check usertype == student (2)
                    self.StudentDashboard(rowId,userFirstName,userLastName,userEmail)
                else:
                    errVar.set("Invalid Username or Password! Try Again.")

LoginPage()