from tkinter import *

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

    def __init__(self):
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
                                                    width=200)

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
        buttons = [
            BtnAnswer(0, self.user_answer),
            BtnAnswer(1, self.user_answer),
            BtnAnswer(2, self.user_answer),
            BtnAnswer(3, self.user_answer),
        ]

        self.button1 = buttons[0]
        self.button1.grid(row=2, column=0, padx=20, pady=20)

        self.button2 = buttons[1]
        self.button2.grid(row=2, column=1, padx=20, pady=20)

        self.button3 = buttons[2]
        self.button3.grid(row=3, column=0, padx=20, pady=20)

        self.button4 = buttons[3]
        self.button4.grid(row=3, column=1, padx=20, pady=20)

        self.window.mainloop()

    def user_answer(self, btn_id):
        is_right = True
        print(btn_id)
        return is_right
