from random import randint

RULES = "What number is missing in the progression?"


def generate_progression(num1, step, lenght):
    progression = []

    for i in range(lenght):
        element = num1 + i * step
        progression.append(element)
    return progression


def generate_question():
    lenght = randint(5, 10)
    num1 = randint(1, 10)
    step = randint(1, 10)
    progression = generate_progression(num1, step, lenght)

    hidden_index = randint(0, lenght - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    progression_str = str(progression)
    question = ''.join(progression_str)
    return question, correct_answer