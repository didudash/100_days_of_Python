from art import logo
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

def coffee_machine():
    print(logo)
    is_on = True
    drinks = menu.get_items()
    while is_on:
        choice = input(f"What would you like? ({drinks}): ")
        if choice == "off":
            is_on = False
            continue
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue 
        else: 
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

coffee_machine()