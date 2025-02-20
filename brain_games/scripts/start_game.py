from brain_games.games import (
    brain_calc,
    brain_even,
    brain_gcd,
    brain_prime,
    brain_progression,
)
from brain_games.scripts.game_engine import run_game


def main():
    print("Choose a game:")
    print("1. - Brain Calc")
    print("2. - Brain Even")
    print("3. - Brain GCD")
    print("4. - Brain Progression")
    print("5. - Brain Prime")

    choice = input("Enter the number of the game: ")

    if choice == "1":
        run_game(brain_calc)
    elif choice == "2":
        run_game(brain_even)
    elif choice == "3":
        run_game(brain_gcd)
    elif choice == "4":
        run_game(brain_progression)
    elif choice == "5":
        run_game(brain_prime)

    else:
        print("Invalid choice. Please enter 1 or 2 or 3 or 4.")


if __name__ == "__main__":
    main()