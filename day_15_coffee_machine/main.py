from art import logo

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COIN_VALUES = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.1,
    "quarters": 0.25,
}


def get_coffee_ingredients(menu, coffee_choice):
    return menu[coffee_choice]["ingredients"]


def get_coffee_cost(menu, coffee_choice):
    return menu[coffee_choice]["cost"]


def compute_resources_after_order(remaining_resources, coffee_ingredients):
    return {
        key: remaining_resources[key] - coffee_ingredients.get(key, 0)
        for key in remaining_resources
    }


def are_resources_sufficient(remaining_resources, coffee_ingredients):
    updated_resources = compute_resources_after_order(
        remaining_resources, coffee_ingredients
    )
    return all(value >= 0 for value in updated_resources.values()), updated_resources


def collect_coins_and_compute_total():
    total_amount = 0
    for coin, value in COIN_VALUES.items():
        count = float(input(f"How many {coin}? "))
        total_amount += count * value
    return total_amount


def print_resources_report(remaining_resources):
    for key, value in remaining_resources.items():
        print(f"{key}: {value}g")


def coffee_machine():
    print(logo)
    current_resources = resources.copy()
    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == "report":
            print_resources_report(current_resources)
            continue
        elif choice == "off":
            is_on = False
            continue

        if choice in MENU:
            ingredients_needed = get_coffee_ingredients(MENU, choice)
            sufficient, updated_resources = are_resources_sufficient(
                current_resources, ingredients_needed
            )

            if sufficient:
                print("Please insert coins.")
                amount_paid = collect_coins_and_compute_total()
                coffee_price = get_coffee_cost(MENU, choice)

                if amount_paid >= coffee_price:
                    change = amount_paid - coffee_price
                    print(f"Here is your ${round(change, 2)} in change.")
                    print(f"Here is your {choice} Enjoy!")
                    current_resources = updated_resources
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry, not enough resources for your order!")
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    coffee_machine()
