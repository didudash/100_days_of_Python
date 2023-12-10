from typing import List
from art import logo, vs
from game_data import data
import random
import os


def choose_random_couple() -> dict:
    a_random = random.randint(0, len(data) - 1)
    b_random = random.randint(0, len(data) - 1)

    while a_random == b_random:
        b_random = random.randint(0, len(data) - 1)
    random_couple = {"A": a_random, "B": b_random}
    return random_couple


def compare_message(random_couple: dict, data: List[dict], vs: str) -> None:
    print(
        f"Compare A: {data[random_couple['A']]['name']},"
        + f" a {data[random_couple['A']]['description']},"
        + f" from {data[random_couple['A']]['country']}."
    )
    print(vs)
    print(
        f"Against B: {data[random_couple['B']]['name']},"
        + f" a {data[random_couple['B']]['description']},"
        + f" from {data[random_couple['B']]['country']}."
    )


def compare_and_return_winner(random_couple, data) -> str:
    follower_count_a = data[random_couple["A"]]["follower_count"]
    follower_count_b = data[random_couple["B"]]["follower_count"]

    if follower_count_a > follower_count_b:
        return "A"
    else:
        return "B"
    # what about ties?


def game() -> None:
    keep_playing = True
    user_score = 0
    while keep_playing:
        os.system("clear")
        print(logo)
        random_couple = choose_random_couple()
        compare_message(random_couple, data, vs)
        winner_letter = compare_and_return_winner(random_couple, data)
        user_choice_letter = input("Who has the more followers? Type 'A' or 'B': ")
        if winner_letter == user_choice_letter:
            user_score += 1
            print(f"You're right! Current score: {user_score}")
            keep_playing = True
        else:
            os.system("clear")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {user_score}")
            keep_playing = False


if __name__ == "__main__":
    game()
