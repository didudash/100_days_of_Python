#1. Create a greeting for your program.
print('Hello! Welcome to the "Band Name Generator" Program')

#2. Ask the user for the city that they grew up in.
city = input("Please input the city where you grew up:\n")

#3. Ask the user for the name of a pet.
pet = input("Also, what's the name of your most loved pet:\n")

#4. Combine the name of their city and pet and show them their band name.
band = city + " " + pet + " " + "Rollinga"

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
print(f"Your band name could be:\n{band}")