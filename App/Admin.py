import tkinter as tk
import csv

class Admin:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("550x300")
        self.f3 = tk.Frame(self.root, bg='green')
        self.f1.place(x=0, y=0, width=800, height=400)

        self.b3 = tk.Button(self.f3, text="User Register", bg='blue',command=self.userRegister)
        self.b3.place(x=250, y=100, width=100, height=50)

        self.b4 = tk.Button(self.f3, text="Exit", bg='red',command=self.root.destroy)
        self.b4.place(x=125, y=100, width=100, height=50)

        self.b5 = tk.Button(self.f3, text="Upload Questions", bg='yellow',command=self.uploadQuestion)
        self.b5.place(x=375 , y=100, width=100, height=50)
        self.root.mainloop()



    def userRegister(self):
        self.c1()


    def uploadQuestion(self):
        self.a1()