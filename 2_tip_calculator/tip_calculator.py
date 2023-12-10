#Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings
#Tip Calculator 

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

#rounded to two decimal places 
person_fee = round(float(bill)*(int(percentage)/100 + 1)/int(people),2)

#with this notation you get 2 decimal places even if it is a $55.00 for instance 
print(f"Each person should pay: ${person_fee:.2f}")