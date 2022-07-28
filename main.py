MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
# The stock:
WATER = 300  # ml
MILK = 200  # ml
COFFEE = 100  # g
MONEY_IN_MACHINE = 0  # $0
coffee_emoji = '☕'

# TODO: The user can chose between: off ( to turn of the machine),
# TODO (espresso/latte/cappuccino),
# TODO report(to see the total report of the machine)

orders = {
    "off": coffee_emoji,
    "espresso": "to order espresso",
    "latte": " to order espresso",
    "cappuccino": " to order cappuccino",
    "report": " to see the report of the machine"
}


# TODO: Check resources sufficient?
def resources(order):
    """ Check resources sufficient? """
    amount_of_water = MENU[order]["ingredients"]["water"]
    amount_of_coffee = MENU[order]["ingredients"]["water"]
    amount_of_milk = MENU[order]["ingredients"]["milk"]
    the_cost = MENU[order]["cost"]
    if (amount_of_water >= WATER and amount_of_milk >= MILK) and (amount_of_coffee >= COFFEE and the_cost > MONEY_IN_MACHINE):
        return True
    elif amount_of_water < WATER:
        return "Sorry there is not enough water."
    elif amount_of_coffee < COFFEE:
        return "Sorry there is not enough water."
    elif amount_of_milk < MILK:
        return "Sorry there is not enough water."



def report():
    """ display The stock """
    print(f"Water: {WATER}ml")
    print(f"Milk: {MILK}ml")
    print(f"Coffee: {COFFEE}g")
    print(f"Money: ${MONEY_IN_MACHINE}")


# TODO Process coins.
def check_payment(coffee):
    """ Process coins """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    the_coffee_cost = MENU[coffee]["cost"]
    total_pay = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    if total_pay >= the_coffee_cost:
        return total_pay - the_coffee_cost
    else:
        return False


def mix_the_ingredients(type_of_coffee):
    """ take the type of coffee as input and subtract the amounts of water, milk, coffee, and the cost from the
    machine of coffee """
    global WATER, MILK, COFFEE, MONEY_IN_MACHINE

    amount_of_water = MENU[type_of_coffee]["ingredients"]["water"]
    amount_of_coffee = MENU[type_of_coffee]["ingredients"]["water"]
    amount_of_milk = MENU[type_of_coffee]["ingredients"]["milk"]
    the_cost = MENU[type_of_coffee]["cost"]

    WATER -= amount_of_water
    MILK -= amount_of_milk
    COFFEE -= amount_of_coffee
    MONEY_IN_MACHINE += the_cost


# TODO Make Coffee
def make_coffee():
    order = input(" What would you like? (espresso/latte/cappuccino): ")
    while order != 'off':
        if order == 'report':
            report()
        elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
            if (resources(order)) == True and (check_payment(order) is not False):
                mix_the_ingredients(order)
                print()
            elif check_payment(order) is False:
                print("Sorry that's not enough money. Money refunded")
            elif resources(order) != True:
                print(resources(order))
            else:
                print("Sorry that's not enough money. Money refunded.")
        order = input(" What would you like? (espresso/latte/cappuccino): ")
