
from tkinter import *
from Login import LoginPage

class Register:
    def __init__(self):

        root = Tk()
        self.LoginPage = LoginPage

        register_canvas = Canvas(root, width=720, height=440, bg="blue")
        register_canvas.pack()

        landing_frame = Frame(register_canvas, bg="white")
        landing_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(landing_frame, text="User Registration", fg="black", bg="white")
        heading.config(font=('calibri 30'))
        heading.place(relx=0.2, rely=0.1)

        button1 = Button(landing_frame, text='Back To Login', borderwidth=1, relief='solid',command=self.register)
        button1.place(relx=0.3, rely=0.4)

        root.mainloop()

    def register(self):
        self.LoginPage()
