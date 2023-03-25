import tkinter as tk
from tkinter import filedialog
import csv
from Database import Database

class CsvUpload:
    def __init__(self):
        # self.master = master
        self.root = tk.Tk()
        self.root.title("CSV Uploader")
        self.database = Database

        self.file_path_label = tk.Label(self.root, text="No file selected.")
        self.file_path_label.pack()

        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack()

        self.upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file)
        self.upload_button.pack()
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


# root = tk.Tk()
# # app = CsvUploader(root)
# root.mainloop()