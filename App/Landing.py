import tkinter as tk
import tkinter.messagebox
import mysql.connector
from tkinter import *
from Login import LoginPage
from Register import Register

import random
import csv
import os

class LandingPage:
    def __init__(self):

        landingPage = Tk()

        self.login = LoginPage
        self.register = Register

        landing_canvas = Canvas(landingPage, width=720, height=440, bg="blue")
        landing_canvas.pack()

        landing_frame = Frame(landing_canvas, bg="white")
        landing_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(landing_frame, text="University of Kelaniya", fg="black", bg="white")
        heading.config(font=('calibri 30'))
        heading.place(relx=0.2, rely=0.1)

        # Format the labels

        button1 = tkinter.Button(landing_frame, text='Admin Login', borderwidth=1, relief='solid',command=self.login)
        button2 = tkinter.Button(landing_frame, text='Student Login', borderwidth=1, relief='solid',command=self.login )
        button3 = tkinter.Button(landing_frame, text='Register', borderwidth=1, relief='solid',command=self.register )

        button1.place(relx=0.3, rely=0.4)
        button2.place(relx=0.3, rely=0.6)
        button3.place(relx=0.3, rely=0.8)

        landingPage.mainloop()

        def login(self):
            self.login()

        def register(self):
            self.Register()


LandingPage()
