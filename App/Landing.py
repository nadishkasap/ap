import tkinter.messagebox
import mysql.connector
import tkinter as tk
from tkinter import *
from Login import LoginPage
from Register import Register

import random
import csv
import os

class LandingPage:
    def __init__(self):

        #global landingPage

        # self.root = tk.Tk()
        # self.root.destroy()

        self.landingPage = tk.Tk()

        self.login = LoginPage
        self.register = Register

        self.landingPage.title("Langing Page - LMS University of Kelaniya")

        landing_canvas = Canvas(self.landingPage, width=720, height=440, bg="#600")
        landing_canvas.pack()

        landing_frame = Frame(landing_canvas, bg="white")
        landing_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(landing_frame, text="University of Kelaniya", fg="black", bg="white")
        heading.config(font=('calibri 30'))
        heading.place(relx=0.2, rely=0.1)

        # Format the labels



        adminLogin = tkinter.Button(landing_frame, text='Login to LMS', borderwidth=1, relief='solid',command=self.login)
        adminLogin.place(x=250, y=150, width=100, height=50)

        register = tkinter.Button(landing_frame, text='Register', borderwidth=1, relief='solid',command=self.register, bg='green' )
        register.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
        register.place(x=250, y=250, width=100, height=50)



        self.landingPage.mainloop()

        def login(self):
            self.login()
            self.landingPage.destroy(self)



        def register(self):
            self.Register()
            self.landingPage.withdraw(self)


LandingPage()
