import tkinter as tk
from tkinter import *
from Database import Database
from tkinter import messagebox

import json

class Exam:
    def __init__(self,rowId,userFirstName,userLastName,userEmail,examIDvar):

        self.rowId = rowId
        self.userFirstName = userFirstName
        self.userLastName = userLastName
        self.userEmail = userEmail
        self.examIDvar = examIDvar

        self.database = Database

        global sup

        sup = Tk()

        # get the data from the json file
        with open('data.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        global question, options, answer

        question = (data['question'])

        print(len(question))

        options = (data['options'])
        self.answer = (data['answer'])

        # create an object of the Quiz Class.
        # quiz = Exam()

        sup.attributes('-fullscreen', True)  # make main window full-screen
        sup.title(" Exam - LMS University of Kelaniya")

        sup_canvas = Canvas(sup, width=720, height=440, bg="#600")
        sup_canvas.pack(fill=tk.BOTH, expand=True)
        sup_canvas.pack()

        global sup_frame

        sup_frame = Frame(sup_canvas, bg="white")
        sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


        #Exam heading
        heading = Label(sup_frame,  text=' EXAM: Advanced Programming ', fg="white", bg="#101357",width=60)
        heading.config(font=('Arial 22'))
        heading.place(relx=0.5, rely=.05, anchor=CENTER)
        heading.config(text=self.examIDvar)

        ### START QUIZ FRAME ####
        global  quiz_frame
        quiz_frame = Frame(sup_canvas, bg="#DBE4C6")
        quiz_frame.place(relwidth=0.5, relheight=0.5, relx=0.24, rely=0.2)
        global frameTextBg
        frameTextBg = "#DBE4C6"

        # BTN Finish Exam
        # sp = Button(sup_frame, text='Finish Exam', padx=5, pady=5, width=5,  bg='green', command=sup.destroy)
        # sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
        # sp.place(relx=0.4, rely=0.85)

        # set question number to 0
        self.q_no = 0

        # assigns ques to the display_question function to update later.
        self.display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected = IntVar(sup)
        self.opt_selected.set(0)

        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts = self.radio_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.buttons()

        # no of questions
        self.data_size = len(question)

        # keep a counter of correct answers
        self.correct = 0

        sup.mainloop()

    def display_result(self):

        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        quiz_frame.destroy()
        global examStatus

        if(score<50):
            passFailLabel = "Sorry you failed! Try again."
            passFailColor = 'red'
            examStatus = "Fail"
        else:
            passFailLabel = "Congratulations! You pass the exam."
            passFailColor = 'green'
            examStatus = "Pass"
        # Exam heading
        heading = Label(sup_frame, text=passFailLabel, fg=passFailColor, bg="white")
        heading.config(font=('Arial 22'))
        heading.place(relx=0.5, rely=.2, anchor=CENTER)

        correctLable = Label(sup_frame, text=correct,  bg="white", fg="green")
        correctLable.config(font=('arial 14'))
        correctLable.place(relx=0.5, rely=.3, anchor=CENTER)

        wrongLable = Label(sup_frame, text=wrong, bg="white", fg="red")
        wrongLable.config(font=('arial 14'))
        wrongLable.place(relx=0.5, rely=.35, anchor=CENTER)

        resultLable = Label(sup_frame, text=result, bg="white")
        resultLable.config(font=('arial 20 bold'))
        resultLable.place(relx=0.5, rely=.45, anchor=CENTER)

        #BTN Finish Exam
        sp = Button(sup_frame, text='Finish Exam', padx=4, pady=4, width=30,  bg='green', fg="white", command=sup.destroy)
        sp.configure(width=30, height=2, activebackground="#33B5E5", relief=FLAT)
        sp.place(relx=0.4, rely=0.6)

        #Saving the results

        try:
            db = self.database('localhost', 'root', '', 'quiz')
            conn = db.connect()
            cursor = db.connection.cursor()
            insertQuery = """INSERT INTO exam_marks (user_id,exam_id,marks,Status) VALUES (%s, %s, %s,%s)"""
            val = (self.rowId,self.examIDvar, score, examStatus)
            cursor.execute(insertQuery, val)
            db.connection.commit()

        except ConnectionError as e:
            print(e)

        self.afterExam()

    def afterExam(self):
        print("after Exam Saving Results to ")

    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):

        if self.opt_selected.get() == self.answer[q_no]:
            messagebox.showinfo("Correct", "Hurray! You answer is correct!")
            return True
        else:
            correctQuiz = "Question: "+ question[self.q_no]
            correctAns = "Correct answer: " + options[self.q_no][self.answer[q_no]-1]

            messagebox.showwarning("wrong","WRONG Answer! \n\n"+correctQuiz+"\n\n"+correctAns)
            #print("Current Question: \t ",question[self.q_no])
            #print("Correct Answer: \t",options[self.q_no][self.answer[q_no]-1])

    def next_btn(self):

        # Check if the answer is correct
        if self.check_ans(self.q_no):
            # if the answer is correct it increments the correct by 1
            self.correct += 1

        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:

            # if it is correct then it displays the score
            self.display_result()

            # destroys the GUI
            #quiz_frame.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()

    def buttons(self):

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(quiz_frame, text="Next", command=self.next_btn,
                             width=20, bg="blue", fg="white", font=("ariel", 16, "bold"), )

        # placing the button  on the screen
        next_button.place(x=200, y=330)

        # This is the second button which is used to Quit the GUI
        quit_button = Button(quiz_frame, text="Quit", command=self.completeExam,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=600, y=330)

    def completeExam(self):
        quiz_frame.destroy()
    def display_options(self):
        val = 0

        # deselecting the options
        self.opt_selected.set(0)

        #print("options[self.q_no]",options[self.q_no])
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # This method shows the current Question on the screen
    def display_question(self):

        # setting the Question properties
        q_no = Label(quiz_frame, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w',  bg=frameTextBg)

        # placing the option on the screen
        q_no.place(x=70, y=50)

    def radio_buttons(self):

        # initialize the list with an empty list of options
        q_list = []

        # position of the first option
        y_pos = 150

        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            #print("opt_selected",self.opt_selected)
            #print("value", len(q_list) + 1)
            radio_btn = Radiobutton(quiz_frame, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14),bg=frameTextBg)

            # adding the button to the list
            q_list.append(radio_btn)
            #print(q_list)

            # placing the button
            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list

#Exam(2,"Saman","Perera","test","FGSMIT2021")