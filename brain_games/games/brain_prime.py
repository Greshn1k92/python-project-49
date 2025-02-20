from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = randint(1, 10)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer