from html import unescape


class QuizBrain:
    def __init__(self, q_list):

        # Initialize QuizBrain with question number, score, question list and current question
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):

        # Check if there are more questions in the question list
        return self.question_number < len(self.question_list)

    def next_question(self):

        # Get the next question, decode HTML entities, and return formatted question text
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer) -> bool:

        # Returns true and updates the score if the user's answer is correct and false otherwise
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            correct = True
        else:
            correct = False
        return correct
