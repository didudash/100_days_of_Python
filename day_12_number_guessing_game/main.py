from art import logo
import random
import os

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
LOWER_BOUND = 1
UPPER_BOUND = 100


def welcome_message() -> str:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")


def get_difficulty() -> str:
    return input("Choose a difficulty. Type 'easy' or 'hard': ")


def guess_number(number_to_guess: int, attempts: int) -> str:
    while True:
        try:
            print(f"You have {attempts} to guess the number.")
            user_guess = int(input("Make a guess: "))

            if user_guess == number_to_guess:
                print("Congratulations! You guessed the number correctly.")
                break
            elif user_guess < number_to_guess:
                print("Too low!")
                print("Guess again.")
                attempts -= 1
            else:
                print("Too high!")
                print("Guess again.")
                attempts -= 1
        except ValueError:
            print("Please enter a valid integer!")


def game():
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
