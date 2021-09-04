class Question:

    def __init__(self, q_text, q_correct_answer, q_incorrect_answers):
        self.text = q_text
        self.answers = []
        self.answers = [{"answer": q_correct_answer,
                        "correct": True}]
        self.incorrect_answers = [{"answer": answer, "correct": False}
                                  for answer in q_incorrect_answers]
        self.answers.extend(self.incorrect_answers)
