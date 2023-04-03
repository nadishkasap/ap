import tkinter as tk
from tkinter import *
from Database import Database



class StudentResults:
    def __init__(self,rowId,userFirstName,userLastName):

        self.database = Database

        self.rowId = rowId
        self.userFirstName = userFirstName
        self.userLastName = userLastName


        global supwin
        supwin = tk.Tk()
        supwin.attributes('-fullscreen', True)
        supwin.title("Student Results")

        sup_canvas_dash = Canvas(supwin, width=720, height=440, bg="#600")
        sup_canvas_dash.pack(fill=tk.BOTH, expand=True)
        sup_canvas_dash.pack()

        sup_frame = Frame(sup_canvas_dash, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        heading = Label(sup_frame, text="Student Results", fg="black", bg="white")
        heading.config(font=('calibri 40'))
        heading.place(relx=0.2, rely=0.1)
        heading.config(text="Results - " + self.userFirstName+ " " +self.userLastName)

        # Quite Button
        quit_button = Button(sup_frame, text="X", command=supwin.destroy, width=5, bg="black", pady=10, padx=3, fg="white", font=("ariel", 16, " bold"))
        quit_button.place(relx=.98, rely=.02, anchor="ne")

        #Student ID
        lblStudentId = Label(sup_frame, text="Student Id : ", fg="black", bg="white")
        lblStudentId.config(font=('calibri 16'))
        lblStudentId.place(relx=0.2, rely=0.3)

        valStudentId = Label(sup_frame, text=self.rowId, fg="black", bg="white")
        valStudentId.config(font=('calibri 16'))
        valStudentId.place(relx=0.5, rely=0.3)

        supwin.mainloop()