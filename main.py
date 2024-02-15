from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu_obj = Menu()
money = MoneyMachine()
answer = input("What would you like? (espresso/latte/cappuccino):")

while answer != "off":
    if answer == "report":
        machine.report()
        money.report()
    else:
        drink = menu_obj.find_drink(answer)
        if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                machine.make_coffee(drink)
    answer = input("What would you like? (espresso/latte/cappuccino):")

