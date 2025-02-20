from random import  randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def generate_question():
    number = randint(1, 10)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer