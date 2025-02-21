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
