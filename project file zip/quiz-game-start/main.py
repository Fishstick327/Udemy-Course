from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Questions(q_text, q_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")