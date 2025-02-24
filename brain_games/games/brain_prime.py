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