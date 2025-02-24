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

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    print(RULES)

    correct_answer_count = 0

    while correct_answer_count < 3:
        question, correct_answer = generate_question()
        print(f'Question: {question}')
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()