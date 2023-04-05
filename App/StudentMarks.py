from tkinter import *
import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
import csv
from Database import Database

class StudentMarks:
    def __init__(self):
        # self.master = master

        self.root = tk.Tk()
        self.root.title("Student Marks")
        s = ttk.Style()
        s.theme_use('clam')
        self.database = Database

        db = self.database('localhost', 'root', '', 'quiz')
        db.connect()
        cursor = db.connection.cursor()
        selectQuery = "SELECT * FROM user INNER JOIN exam_marks ON user.id = exam_marks.user_id WHERE user.userType=2"
        cursor.execute(selectQuery)
        results = cursor.fetchall()

        tree = ttk.Treeview(self.root, column=("c1", "c2", "c3","C4","C5"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="FName")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="LName")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Exam")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="Marks %")
        j=0
        for x in results:
            j=j+1
            print(x)
            tree.insert('', 'end', text=j, values=(j, x[1], x[2],x[9],x[10]))

        tree.pack()

        ex_canvas = Canvas(self.root, width=720, height=440, bg="#600")
        ex_canvas.pack(fill=ttk.BOTH, expand=True)
        ex_canvas.pack()

        ex_frame = Frame(ex_canvas, bg="white")
        ex_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        # file upload heading
        heading = Label(ex_frame, text='Student Marks', fg="white", bg="#101357", width=60)
        heading.config(font=('Arial 22'))
        heading.place(relx=0.5, rely=.1, anchor=CENTER)

        self.root.mainloop()

