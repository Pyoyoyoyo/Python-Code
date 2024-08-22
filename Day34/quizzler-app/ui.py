from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font="Arial 12 normal")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(self.window, bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text((150, 125),text="Hello Everyone", width=280,
                                                     fill=THEME_COLOR, justify="center", font="Arial 14 italic")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(self.window, image=true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(self.window, image=false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

