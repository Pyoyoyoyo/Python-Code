from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    choice = input(f"​What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee):
            payment = money_machine.make_payment(coffee.cost)
            if payment:
                coffee_maker.make_coffee(coffee)

