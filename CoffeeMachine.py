from Coffeedata import MENU, resources, profit

def check_res(pmt):
    if resources["water"] < MENU[pmt]['ingredients']["water"]:
        print("Not enough water")
        return False
    elif resources["milk"] < MENU[pmt]['ingredients']["milk"]:
        print("Not enough Milk")
        return False
    elif resources['coffee'] < MENU[pmt]['ingredients']['coffee']:
        print("Not enough coffee")
        return False
    else:
        return True

def proc_coins():
    print("Please insert coins")
    q = int(input("How many Quarters: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickels: "))
    p = int(input("How many pennies: "))
    money = float((q*0.25)+(d*0.1)+(n*0.05)+(p*0.01))

    return money

def check_trans(money, pmt):
    if money < MENU[pmt]['cost']:
        print("Insufficient funds")
        return False
    else:
        profit = MENU[pmt]['cost']
        print(f"Here is ${round(money - MENU[pmt]['cost'], 2)} change")
        return True

def make_c(pmt):
    resources["water"] -= MENU[pmt]['ingredients']['water']
    resources["milk"] -= MENU[pmt]['ingredients']['milk']
    resources["coffee"] -= MENU[pmt]['ingredients']['coffee']
    resources["money"] += MENU[pmt]['cost']
    print(f"Here is your {pmt}, Enjoy!")

is_on = True

while is_on:
    pmt = str(input("what would you like? (espresso/latte/cappuccino)"))
    if pmt.lower() == "off":
        is_on = False
    elif pmt.lower() == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    else:
        if check_res(pmt):
            if check_trans(proc_coins(), pmt):
                make_c(pmt)

