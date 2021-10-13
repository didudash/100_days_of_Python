#Rock, Paper, Scissors game 
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#randomly choose for the computer 
choice_computer = random.randint(0,2)

#Logic

#rock: 0
#paper: 1
#scissors : 2
game_choices = [rock, paper, scissors]
if choice < 0 or choice > 2:
    print("You typed an invalid number, you lose")
else:
    choice_user = choice
    print(game_choices[choice_user])
    print(f"Computer chose: {game_choices[choice_computer]}")

    if choice_user == choice_computer: 
        print("It's a draw")
    elif choice_user == 0 and choice_computer == 2: 
        print("You win")
    elif choice_computer == 0 and choice_user == 2: 
        print("You lose")
    elif choice_user > choice_computer:
        print("You win")
    elif choice_computer > choice_user:
        print("You lose")
