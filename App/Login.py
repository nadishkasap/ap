import tkinter as tk
import tkinter.messagebox
import mysql.connector
from Admin import Admin
import random
import csv
import os

class LoginPage:
    def __init__(self):

        self.marks = 0
        self.mycursor=''
        self.admin = Admin

        self.root = tk.Tk()
        self.root.geometry("550x300")
        self.f1 = tk.Frame(self.root, bg='yellow')
        self.f1.place(x=0, y=0, width=800, height=400)
        # username
        self.l1 = tk.Label(self.f1, text='Enter User Name ss:')
        self.l1.place(x=50, y=50)
        self.e1 = tk.Entry(self.f1, width=25, font=("", 12))
        self.e1.place(x=200, y=50)
        # password
        self.l2 = tk.Label(self.f1, text='Enter Passwordss:')
        self.l2.place(x=50, y=100)
        self.e2 = tk.Entry(self.f1, width=25, font=("", 12), show='*')
        self.e2.place(x=200, y=100)
        # buttons
        self.b1 = tk.Button(self.f1, text="LogIn", bg='blue',command=self.LoginClick)
        self.b1.place(x=250, y=150, width=100, height=50)
        self.b2 = tk.Button(self.f1, text="Exit", command=self.root.destroy, bg='red')
        self.b2.place(x=100, y=150, width=100, height=50)

        self.root.mainloop()

    def LoginClick(self):
        self.admin()
