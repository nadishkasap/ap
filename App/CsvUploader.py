import tkinter as tk
from tkinter import filedialog
import csv

class CsvUpload:
    def __init__(self):
        # self.master = master
        self.root = tk.Tk()
        self.root.title("CSV Uploader")

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
        file_path = self.file_path_label.cget("text")
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)


# root = tk.Tk()
# # app = CsvUploader(root)
# root.mainloop()