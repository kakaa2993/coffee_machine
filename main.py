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
# The stock:
WATER = 300  # ml
MILK = 200  # ml
COFFEE = 100  # g
MONEY = 0  # $0
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

user_order = input(" What would you like? (espresso/latte/cappuccino): ")
# TODO: Check resources sufficient?
def resources():
    """ Check resources sufficient? """






def report():
    # The stock:
    print(WATER)
    print(MILK)
    print(COFFEE)
    print(MONEY)
    print(coffee_emoji)

# TODO Process coins.


# TODO Make Coffee
def make_coffee(order):
    if order