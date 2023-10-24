
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_ingredients(MENU: dict, coffee_choice:str)-> dict:
   coffee_ingredients = MENU[coffee_choice]['ingredients']
   return coffee_ingredients

def check_cost(MENU: dict, coffee_choice:str)-> float:
    coffee_cost = MENU[coffee_choice]['cost']
    return coffee_cost

def update_remaining_resources(remaining_resources:dict, coffee_ingredients:dict):
    new_resources = {key: remaining_resources[key] - coffee_ingredients.get(key, 0) for key in remaining_resources}
    return new_resources 

# update ooutput 
def check_resources(remaining_resources:dict, coffee_ingredients:dict):
    new_resources = update_remaining_resources(remaining_resources, coffee_ingredients)
    depleted_resources = {key: value for key, value in new_resources.items() if value < 0}
    if depleted_resources:
        has_resources = False
    else: 
        has_resources = True
    return has_resources, depleted_resources

def get_coins()-> float: 
    print("Please insert coins")
    pennies = float(input("How many pennies? "))
    nickels = float(input("How many nickels? "))
    dimes = float(input("How many dimes? "))
    quarters = float(input("How many quarters? "))

    paid_amount = pennies*0.01 + nickels*0.05 + dimes*0.1 + quarters*0.25
    return paid_amount



def print_report(remaining_resources: dict)-> None: 
    for key, value in remaining_resources.items():
        print(f"{key}: {value}")

def machine():

    remaining_resources = resources 
    is_on = True
    while is_on:
        coffee_choice = input("What would you like? (espresso/latte/capuccino): ")
        if coffee_choice == "report":
            print_report(remaining_resources)
        elif coffee_choice == "off":
            is_on = False 
        else: 
            coffee_ingredients = check_ingredients(MENU, coffee_choice)
            has_resources, depleted_resources = check_resources(remaining_resources, coffee_ingredients)
            if has_resources: 
                paid_amount = get_coins()
                coffee_cost = check_cost(MENU, coffee_choice)
                if paid_amount >= coffee_cost: 
                    change = paid_amount - coffee_cost
                    print(f"Here is your ${round(change,1)} in change.")
                    # include coffee emoji 
                    print(f"Here is your {coffee_choice} Enjoy!")
                    remaining_resources = update_remaining_resources(remaining_resources, coffee_ingredients)
                else:
                    print("Sorry that's not enough money. Money refunded.") 
            else: 
                print(f"Sorry there is not enough {', '.join(depleted_resources.keys())}")
                exit()

if __name__ == "__main__":
    machine()
