from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for elem in question_data:

    question = Question(elem['text'], elem['answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    user_answer = quiz_brain.next_question()

print(f"You completed the quiz with {quiz_brain.score}/{quiz_brain.question_number}")


