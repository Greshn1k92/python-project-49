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
    question = ' '.join(map(str, progression))

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