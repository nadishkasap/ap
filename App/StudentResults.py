import tkinter as tk
from tkinter import *
from Database import Database
from tkinter import ttk




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

        db = self.database('localhost', 'root', '', 'quiz')
        db.connect()
        cursor = db.connection.cursor()
        selectQuery = "SELECT * FROM user INNER JOIN exam_marks ON user.id = exam_marks.user_id WHERE user.userType=2"
        cursor.execute(selectQuery)
        results = cursor.fetchall()

        tree = ttk.Treeview(sup_frame, column=("c1", "c2", "c3", "C4", "C5"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="FName")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="LName")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Exam")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="Marks")
        j = 0
        for x in results:
            j = j + 1
            print(x)
            tree.insert('', 'end', text=j, values=(j, x[1], x[2], x[9], x[10]))

        tree.pack()

        supwin.mainloop()