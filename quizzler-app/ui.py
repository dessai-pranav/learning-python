from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.window = Tk()
        self.quiz = quiz
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score_label = Label(self.window,text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(self.window, bg="white",width=300, height=250)
        self.canvas.create_text(150, 125, text="some question",width=280, fill=THEME_COLOR,font=("Arial",25,"italic"))
        self.canvas.grid(row=1, column=0,columnspan=1,pady=50)
        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true.grid(row=2, column=0,)
        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.false.grid(row=2, column=1,)
        self.get_next_question()





        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.quiz.text, text=q_text)

    def true_pressed(self):
        self.quiz.check_answer("True")
    def false_pressed(self):
        self.quiz.check_answer("False")


