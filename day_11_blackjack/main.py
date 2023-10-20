# It has a limited size of deck
# All the cards have the same probability of being drawn


import random
import string
from typing import List
import os
from art import logo


def deal_card() -> int:
    """Return one random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards: List[int]) -> int:
    """Receive as input the list of cards
    Checks if there is a blackjack and checks for aces
    Outputs the corresponding score with those cards"""
    # Blackjack with 2 cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Case in which there is an ace and overflow
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_scores(user_score: int, dealer_score: int) -> str:
    """Compare user and dealer scores and return the game outcome."""
    # Both have a Blackjack
    if user_score == 0 and dealer_score == 0:
        return "It's a Draw! Both have a Blackjack!"
    elif dealer_score == 0:
        return "You lose, the dealer has a Blackjack"
    elif user_score == 0:
        return "You win!! with a Blackjack"
    elif user_score == dealer_score:
        return "It's a Draw!"
    elif user_score > 21:
        return "You lose, you went over"
    elif dealer_score > 21:
        return "You win! the dealer went over"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose"


def game():
    # Prints game art
    print(logo)

    user_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(
            f"   Your cards are: {', '.join(map(str, user_cards))}, and your current score is: {user_score} "
        )
        print(f"   The dealer's first card is: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_wants_to_continue = input(
                "Type 'y' to get another card, type 'n' to pass: "
            )
            if user_wants_to_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

        # The dealer's strategy after the first two cards
        while (
            dealer_score != 0 and dealer_score < 17 and user_score != 0
        ):  # Added condition here
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

    print(
        f"   Your final hand: {', '.join(map(str, user_cards))}, final score: {user_score}"
    )
    print(
        f"   The dealer's final hand: {', '.join(map(str, dealer_cards))}, final score: {dealer_score}"
    )
    print(compare_scores(user_score, dealer_score))


if __name__ == "__main__":
    while (
        input(
            "Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: "
        )
        == "y"
    ):
        os.system("clear")
        game()
