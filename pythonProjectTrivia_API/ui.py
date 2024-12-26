from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)



        # Cria o canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.card_question = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Ahhhhhhhhh",
                                                     font=FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        # Crias os botões
        img_true = PhotoImage(file="images/true.png")
        img_false = PhotoImage(file="images/false.png")
        self.true_button = Button(image=img_true, highlightthickness=0,command=self.press_true)
        self.false_button = Button(image=img_false, highlightthickness=0,command=self.press_false)
        self.true_button.grid(row=3, column=1)
        self.false_button.grid(row=3, column=2)
        # Cria o label
        self.score_label = Label(text="Score | 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=2)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.card_question, text=q_text)
        else:
            self.canvas.itemconfig(self.card_question, text="You're reached the end of the quiz!.")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def press_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


