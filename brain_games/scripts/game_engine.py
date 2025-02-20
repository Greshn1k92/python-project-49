def run_game(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULES)

    correct_answer_count = 0

    while correct_answer_count < 3:
        question, correct_answer = game.generate_question()
        print(f'Question: {question}')
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")