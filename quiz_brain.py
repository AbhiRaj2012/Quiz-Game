class QuestionBrain:
    def __init__(self, QuestionList):
        self.question_number = 0
        self.score = 0
        self.question_list = QuestionList

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? : ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
            print(f"Current score is : {self.score}/{self.question_number}")

        else:
            print("That's Wrong!")
        print(F"The correct answer is : {correct_answer}")
        print("\n")

