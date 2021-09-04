import html
import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.current_correct = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        print(self.current_question.answers)
        random.shuffle(self.current_question.answers)
        self.current_correct = [_ for _, value in enumerate(self.current_question.answers) if value["correct"]][0]
        print(self.current_correct)
        self.question_number += 1
        q_text = f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"
        q_answers = [html.unescape(answer["answer"]) for answer in self.current_question.answers]
        return q_text, q_answers

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answers[user_answer]["correct"]
        if correct_answer:
            self.score += 1
            return True, self.current_correct
        else:
            return False, self.current_correct
