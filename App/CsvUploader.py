from tkinter import *
import tkinter as tk
from tkinter import filedialog
import csv
from Database import Database

class CsvUpload:
    def __init__(self):
        # self.master = master

        self.root = tk.Tk()
        self.root.title("CSV Uploader")

        ex_canvas = Canvas(self.root, width=720, height=440, bg="#600")
        ex_canvas.pack(fill=tk.BOTH, expand=True)
        ex_canvas.pack()

        ex_frame = Frame(ex_canvas, bg="white")
        ex_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        # file upload heading
        heading = Label(ex_frame, text='CSV file upload ', fg="white", bg="#101357", width=60)
        heading.config(font=('Arial 22'))
        heading.place(relx=0.5, rely=.1, anchor=CENTER)

        self.database = Database

        self.file_path_label = tk.Label(ex_frame, text="No file selected.",bg="white")
        self.file_path_label.place(relx=0.5, rely=.3, anchor=CENTER)

        self.select_button = tk.Button(ex_frame, text="Select File", command=self.select_file)
        self.select_button.place(relx=0.5, rely=.4, anchor=CENTER)
        self.select_button.configure(width=20, height=2, activebackground="#33B5E5")

        self.upload_button = tk.Button(ex_frame, text="Upload File", command=self.upload_file)
        self.upload_button.place(relx=0.5, rely=.6, anchor=CENTER)
        self.upload_button.configure(width=20, height=2, activebackground="#33B5E5")

        self.root.mainloop()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.file_path_label.config(text=file_path)

    def upload_file(self):
        db = self.database('localhost', 'root', '', 'quiz')
        db.connect()
        cursor = db.connection.cursor()
        file_path = self.file_path_label.cget("text")
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            readerNew = list(reader)
            for row in readerNew[1:]:
                print(row)
                question =row[0]
                answer1 =row[1]
                answer2 =row[2]
                answer3 =row[3]
                answer4 = row[4]
                correctAnswer = row[5]
                examType = row[6]
                insertQuery = """INSERT INTO question (question, answer1, answer2,answer3,answert4,correctAnswer,examType) VALUES (%s, %s, %s,%s,%s,%s,%s)"""
                val = (question, answer1, answer2, answer3, answer4,correctAnswer,examType)
                cursor.execute(insertQuery, val)
                db.connection.commit()
