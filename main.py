from question_model import Question
from data import question_data
import quiz_brain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

Quiz = quiz_brain.QuestionBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {Quiz.score}/{Quiz.question_number}")

input("Press Enter to close the program...")