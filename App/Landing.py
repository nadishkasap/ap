import tkinter.messagebox
import tkinter as tk
from tkinter import *
from Login import LoginPage
from Register import Register
from PIL import Image, ImageTk
import os

class LandingPage:
    def __init__(self):

        global landingPage

        landingPage = tk.Tk()
        landingPage.attributes('-fullscreen', True)  # make main window full-screen

        self.login = LoginPage
        self.register = Register

        landingPage.title("Langing Page - LMS University of Kelaniya")

        landing_canvas = Canvas(landingPage, width=720, height=440, bg="#600")
        landing_canvas.pack(fill=tk.BOTH, expand=True)
        landing_canvas.pack()

        landing_frame = Frame(landing_canvas, bg="white")
        landing_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(landing_frame, text="University of Kelaniya", bg="white", fg='#560600')
        heading.config(font=('calibri 30'))
        heading.place(relx=0.2, rely=0.1)

        ###Quite Button
        quit_button = Button(landing_frame, text="X", command=landingPage.destroy, width=5, bg="black",pady=10,padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        frame = Frame(landing_canvas, width=500, height=350, bg="red")
        frame.pack()
        frame.place(anchor='center', relx=0.65, rely=0.5)

        im = Image.open(os.getcwd()+"/images/landing_bg.jpg")
        ph = ImageTk.PhotoImage(im)

        label = Label(frame, image=ph,width=550, height=350, bg="white")
        label.image = ph
        label.pack()


        adminLogin = tkinter.Button(landing_frame, text='Login to EMS', borderwidth=1, relief='solid',command=self.login, fg="green",font=('Georgia 16'))
        adminLogin.place(x=250, y=250, width=200, height=50)

        register = tkinter.Button(landing_frame, text='Register', borderwidth=1, relief='solid',command=self.register, bg='green',font=('Georgia 16'), fg="white" )
        register.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
        register.place(x=250, y=350, width=200, height=50)


        landingPage.mainloop()

        def login(self):
            landingPage.destroy()
            self.login()


        def register(self):
            landingPage.destroy()
            self.Register()



LandingPage()
