
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
coins = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickel" : 0.05,
    "pennny" : 0.01,
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True
        
def process_coins():
    print("please insert coin.")
    total = int(input("How Many Quarters?:"))*0.25
    total += int(input("How Many dimes?:"))*0.10
    total += int(input("How Many nickles?:"))*0.05
    total += int(input("How Many pennies?:"))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit +=drink_cost
        return True
    else:
        print("Sorry, you don't have enough money to make this transaction.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your coffee for {drink_name}")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(drink["ingredients"], drink["cost"]):
                make_coffee(choice, drink["ingredients"])
