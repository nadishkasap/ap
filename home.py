import tkinter as tk
from tkinter import *
import random
import sqlite3
import time

import tkinter.messagebox

def Login():
    #sup.destroy()
    global login
    login = Tk()

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login, width=720, height=440, bg="blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Quiz App Login", fg="black", bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Username", fg='black', bg='white')
    ulabel.place(relx=0.21, rely=0.4)
    uname = Entry(login_frame, bg='#d3d3d3', fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.31, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Password", fg='black', bg='white')
    plabel.place(relx=0.215, rely=0.5)
    pas = Entry(login_frame, bg='#d3d3d3', fg='black', show="*", textvariable=password)
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.5)

    login.mainloop()

def LandingPage():
    #sup.destroy()
    global landingPage
    landingPage = Tk()

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(landingPage, width=720, height=440, bg="blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Home Page", fg="black", bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    # Format the labels
    def admin():
        tkinter.messagebox.showinfo('Response', 'Thanks for cliking the button')

    def student():
        tkinter.messagebox.showinfo('Response', 'Thanks for cliking the button')

    button1 = tkinter.Button(login_frame, text='Admin Login', borderwidth=1, relief='solid',command=Login)
    button2 = tkinter.Button(login_frame, text='Student Login', borderwidth=1, relief='solid',command=Login)
    button3 = tkinter.Button(login_frame, text='Register', borderwidth=1, relief='solid', )

    button1.place(relx=0.3, rely=0.4)
    button2.place(relx=0.3, rely=0.6)
    button3.place(relx=0.3, rely=0.8)

   # button1.place(x=100, y=150)
   # button2.place(x=100, y=200)
   # button1.pack(side='top', ipadx=100, ipady=20, padx=20, pady=20, )
   # button2.pack(side='top', ipadx=100, ipady=20, padx=20, pady=20, )



    # Create an instance of the MyGUI class.
    landingPage.mainloop()

LandingPage()

