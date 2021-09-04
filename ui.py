from tkinter import *
from quiz_brain import QuizBrain

COLORS = {
    "MAIN": "#0F044C",
    "SECONDARY": "#141E61",
    "OPT1": "#787A91",
    "OPT2": "#EEEEEE"
}
QUESTION_FONT = ("Arial", 20, "italic")
ANSWER_FONT = ("Arial", 10, "bold")
LOGO_FONT = ("Arial", 40, "bold")
SCORE_FONT = ("Arial", 20)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=COLORS["MAIN"], padx=30, pady=30)

        # Logo placeholder
        self.lbl_logo = Label(text="Quiz APP",
                              bg=COLORS["MAIN"],
                              fg=COLORS["OPT1"],
                              padx=20,
                              pady=20,
                              font=LOGO_FONT)

        self.lbl_logo.grid(row=0, column=0, padx=20, pady=20)

        # Score label
        self.lbl_score = Label(text="Score: 0",
                               bg=COLORS["MAIN"],
                               fg=COLORS["OPT1"],
                               padx=20,
                               pady=20,
                               font=SCORE_FONT)

        self.lbl_score.grid(row=0, column=1, padx=20, pady=20)

        # Question Text
        self.canvas = Canvas(width=600, height=400, bg=COLORS["SECONDARY"], highlightthickness=0)
        self.txt_question = self.canvas.create_text(300,
                                                    200,
                                                    font=QUESTION_FONT,
                                                    fill=COLORS["OPT1"],
                                                    text="Question text",
                                                    width=400)

        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Buttons
        class BtnAnswer(Button):
            def __init__(self, identifier: int, command):
                super().__init__(padx=20,
                                 pady=20,
                                 bg=COLORS["SECONDARY"],
                                 fg=COLORS["OPT1"],
                                 activebackground=COLORS["OPT1"],
                                 activeforeground=COLORS["OPT2"],
                                 text="PlaceHolder",
                                 height=3,
                                 width=30,
                                 font=ANSWER_FONT,
                                 command=lambda: command(identifier))
        self.buttons = [
            BtnAnswer(0, self.user_answer),
            BtnAnswer(1, self.user_answer),
            BtnAnswer(2, self.user_answer),
            BtnAnswer(3, self.user_answer),
        ]

        self.button1 = self.buttons[0]
        self.button1.grid(row=2, column=0, padx=20, pady=20)

        self.button2 = self.buttons[1]
        self.button2.grid(row=2, column=1, padx=20, pady=20)

        self.button3 = self.buttons[2]
        self.button3.grid(row=3, column=0, padx=20, pady=20)

        self.button4 = self.buttons[3]
        self.button4.grid(row=3, column=1, padx=20, pady=20)

        # Fill ui with data
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        for button in self.buttons:
            button.config(bg=COLORS["SECONDARY"])
        self.lbl_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text, q_answers = self.quiz.next_question()
            self.canvas.itemconfig(self.txt_question, text=q_text)
            for index, button in enumerate(self.buttons):
                button.config(text=q_answers[index])
        else:
            self.canvas.itemconfig(self.txt_question, text="You've ended the quiz!")
            for button in self.buttons:
                button.config(state="disable", text="")

    def user_answer(self, btn_id):
        is_right, current_correct = self.quiz.check_answer(btn_id)
        self.give_feedback(is_right, btn_id, current_correct)

    def give_feedback(self, is_right, btn_id, current_correct):
        if is_right:
            color = "Green"
        else:
            color = "Red"
            self.buttons[current_correct].config(bg="Green")
        self.buttons[btn_id].config(bg=color)
        self.window.after(1000, func=self.get_next_question)


