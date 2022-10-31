from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    machine_on = True
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    menu_list = menu.get_items().split("/")
    menu_list.remove("")

    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        # Coffee selected
        if user_input in menu_list:
            drink = menu.find_drink(user_input)
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)

        elif user_input == "report":
            coffee_maker.report()
            money_machine.report()

        elif user_input == "off":
            machine_on = False

        # Invalid input
        else:
            print("Please choose between espresso/latte/cappuccino.")


coffee_machine()
