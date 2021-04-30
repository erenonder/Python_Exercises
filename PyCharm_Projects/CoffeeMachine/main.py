from coffee_data import MENU, resources

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
coins = {"quarters": 0.25, "dimes": 0.1, "nickles": 0.05, "pennies": 0.01}


def check_money(received_money, user_selection):

    transaction_successful = False
    if "money" not in resources.keys():
        resources["money"] = 0

    cost = MENU[user_selection]["cost"]
    if received_money < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] += cost
        if received_money > cost:
            print(f"Here is ${received_money-cost:.2f} dollars in change.")
            transaction_successful = True

    return transaction_successful

def update_resources(user_selection):
    for ingredient in MENU[user_selection]["ingredients"].keys():
        resources[ingredient] -= MENU[user_selection]["ingredients"][ingredient]

def check_resources(user_selection):
    sufficient_resources = True
    for ingredient in MENU[user_selection]["ingredients"].keys():
        if MENU[user_selection]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            sufficient_resources = False

    return sufficient_resources

def ask_user_selection():
    out_of_service = False
    while not out_of_service:
        user_selection = input(r"What would you like? (espresso/latte/cappuccino): ")

        if user_selection == "off":
            out_of_service = True
        elif user_selection == "report":
            print_report()
        elif user_selection in ["espresso", "latte", "cappuccino"]:
            if check_resources(user_selection):
                print("Please insert coins...")
                received_money = 0
                for coin in coins.keys():
                    coin_count = int(input(f"How many {coin}: "))
                    received_money += coins[coin] * coin_count

                if check_money(received_money, user_selection):
                    update_resources(user_selection)
                    print(f"Here is your {user_selection}. Enjoy!")

        else:
            print("Invalid selection. Try again...")

def print_report():
    for key, value in resources.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    ask_user_selection()