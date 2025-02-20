from random import randint

RULES = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while a != b and b != a:
        if a > b:
            a = b % a
        else:
            b = a % b


def generate_question():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    correct_answer = str(num1 - num2)
    questiom = f"{num1} {num2}"
    return questiom, correct_answer


