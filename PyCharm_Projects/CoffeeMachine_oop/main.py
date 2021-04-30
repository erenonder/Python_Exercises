from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

system_on = True

menu = Menu()
coff_maker = CoffeeMaker()
machine = MoneyMachine()

while system_on:
    user_selection = input(f"What would you like? {menu.get_items()}: ")
    if user_selection == "off":
        system_on = False
    elif user_selection == "report":
        coff_maker.report()
        machine.report()
    else:
        item = menu.find_drink(user_selection)
        resource_sufficient = coff_maker.is_resource_sufficient(item)
        if resource_sufficient:
            sufficient_money = machine.make_payment(item.cost)
            if sufficient_money:
                coff_maker.make_coffee(item)
