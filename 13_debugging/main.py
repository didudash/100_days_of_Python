# Debugging Examples

def odd_or_even()-> None: 
    number = int(input()) # Which number do you want to check?

    # Fist error, instead of assignment it should validating 
    # if number % 2 = 0:
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

def leap_year()-> None:
    # Which year do you want to check?

    # If the as in the line bellow it gives a TypeError 
    # year = input()
    year = int(input())

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

def fizzbuzz()-> None:
    target = int(input())
    for number in range(1, target + 1):
        # It was looking for either one of the conditions instead of the two at the same time 
    	# if number % 3 == 0 or number % 5 == 0:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # In the previous version it went into the other options eventhough it was already FizzBuzz
        # if number % 3 == 0:
        elif number % 3 == 0:
            print("Fizz")
        # if number % 5 == 0:
        elif number % 5 == 0:
            print("Buzz")
        else:
            # it was printing the number inside a list 
            # print([number])
            print(number)