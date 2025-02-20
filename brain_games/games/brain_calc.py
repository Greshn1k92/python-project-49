from random import choice, randint

RULES = "What is the result of the expression?"


def generate_question():
    operations = ['+', '-', '*']
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operation = choice(operations)
    question = f"{number1} {operation} {number2}"
    correct_answer = str(eval(question))
    return question, correct_answer

def main():
    generate_question()

if __name__ == "__main__":
    main()