import random
import quizques
logo = r"""
  ___  _   _ ___ ________   _____   _   __  __ _____ 
 / _ \| | | |_ _|_  /  _ \ / _ \ \ / / |  \/  |  ___|

| | | | | | || |  / /| |_) | | | \ V /  | |\/| | |__  
| |_| | |_| || | / / |  _ <| |_| || |   | |  | |  __| 
 \__\_\\___/|___/___||_| \_\\___/ |_|   |_|  |_|_____|
"""
LINE = "******************************************"

class QuizGame:
    def __init__(self, questions, options):
        combined = list(zip(questions, options))
        random.shuffle(combined)
        self.questions, self.options = zip(*combined)
        
        self.score = 0
        self.question_num = 0


    def display_question(self):
        current_q = self.questions[self.question_num]
        print(f"\nQ.{self.question_num + 1}: {current_q['text']}")
        for option in self.options[self.question_num]:
            print(f"  {option}")
        
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        self.check_answer(user_answer, current_q['answer'])

    def check_answer(self, user_answer, correct_answer):
        self.question_num += 1
        if user_answer == correct_answer:
            self.score += 1
            print("✅ Correct!")
        else:
            print("❌ Incorrect.")
            print(f"   The correct answer was: {correct_answer}")
        
        print(f"   Score: {self.score}/{self.question_num}")
        print(LINE)

    def has_questions(self):
        return self.question_num < len(self.questions)
print(logo)
print("Welcome to the Ultimate Quiz Challenge!")
print(LINE)

quiz = QuizGame(quizques.Question_bank, quizques.options)

while quiz.has_questions():
    quiz.display_question()

print("\n" + LINE)
print("🎉 QUIZ COMPLETED!")
print(f"Your Final Score: {quiz.score}/{quiz.question_num}")
final_percent = round((quiz.score / quiz.question_num) * 100)
print(f"Success Rate: {final_percent}%")
print(LINE)
