from random import randint

RULES = "What number is missing in the progression?"

def generate_progression(num1, step, lenght): #генерирует арифметическую прогрессию
    progression = [] #пустой список

    for i in range(lenght):
        element = num1 + i * step #вычисляем каждый элемент
        progression.append(element) #добавялем к списку элемент который вычисляли
    return progression #возвращаем список

def generate_question(): # генерирует прогрессию с пропущенным элементом
    lenght = randint(5, 10)
    num1 = randint(1, 10)
    step = randint(1, 10)
    progression = generate_progression(num1, step, lenght)

    hidden_index = randint(0, lenght -1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    progression_str = str(progression)
    question = ''.join(progression_str)
    return question, correct_answer