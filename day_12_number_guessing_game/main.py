from art import logo
import random
import os

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
LOWER_BOUND = 1
UPPER_BOUND = 100


def welcome_message() -> None:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")


def get_difficulty() -> str:
    return input("Choose a difficulty. Type 'easy' or 'hard': ")


def guess_number(number_to_guess: int, attempts: int) -> None:
    while attempts > 0:
        if attempts == 1:
            print(f"You have {attempts} attempt remaining to guess the number.")
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            user_guess = int(input("Make a guess: "))

            if user_guess == number_to_guess:
                print("Congratulations! You guessed the number correctly.")
                return
            elif user_guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

            attempts -= 1

            # Print "Guess again." only if there are still remaining attempts
            if attempts:
                print("Guess again.")
        except ValueError:
            print("Please enter a valid integer!")

    print("You ran out of attempts.")


def game() -> None:
    welcome_message()
    number_to_guess = random.randint(LOWER_BOUND, UPPER_BOUND)
    difficutly = get_difficulty()
    if difficutly == "easy":
        attempts = EASY_ATTEMPTS
    elif difficutly == "hard":
        attempts = HARD_ATTEMPTS
    else:
        print("Invalid difficulty level entered. Please enter either 'easy' or 'hard'.")
        exit()
    guess_number(number_to_guess, attempts)


if __name__ == "__main__":
    os.system("clear")
    game()
