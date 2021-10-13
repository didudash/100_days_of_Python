#treasure island 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
step_1 = input('You are at a croos road. Where do you want to go? Type "left" or "right"\n')
step_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
step_3 = input('You arrive at the island unharmed. There is a house with 3 doors. Oner red, one yellow and one blue. Which colour do you choose?\n')

if step_1.lower() == 'left':
	if step_2.lower() == 'wait':
		if step_3.lower() == 'red':
			print("You got burned by a fire. GAME OVER.")
		elif step_3.lower() == 'blue':
			print("You got eaten by beasts. GAME OVER.")
		elif step_3.lower() == 'yellow':
			print("You WIN!")
		else: 
			print("GAME OVER.")
	else: 
		print("You have been attacked by a trout. GAME OVER.")
else:
	print("You just fell into a hole. GAME OVER.")

