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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0
status="on"
while (status == "on"):
    choice = input("What would you like to have? Expresso, cappuccino or latte?")
    total = 0
    if choice == "off":
        status = "off"
    elif choice == "report":
        print(resources)
        print("money = ", money)
    elif choice == "espresso":
        if(resources["water"]<50 and resources["coffee"]<18):
            print("not enough water and coffee")
        elif(resources["water"]<50):
            print("not enough water")
        elif(resources["coffee"]<18):
            print("not enough coffee")
        else:
            print("please enter coins")
            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01
            if(total > 1.5):
                print(f"here is {total-1.5}")
                money+=1.5
                print("here is your expresso")
                resources["water"]-=50
                resources["coffee"]-=18
            elif(total == 1.5):
                money += 1.5
                print("here is your expresso")
                resources["water"] -= 50
                resources["coffee"] -= 18
            else:
                print("not enough money. it has been refunded")
    elif choice == "latte":
        if(resources["water"]<200 and resources["coffee"]<24  and resources["milk"]<150):
            print("Not enough water and coffee and milk")
        elif(resources["water"]<200 and resources["coffee"]<24):
            print("not enough water and coffee")
        elif(resources["water"]<200 and resources["milk"]<150):
            print("not enough water and milk")
        elif (resources["coffee"] < 24 and resources["milk"] < 150):
            print("not enough coffee and milk")
        elif(resources["water"]<200):
            print("not enough water")
        elif(resources["coffee"]<24):
            print("not enough coffee")
        elif(resources["milk"]<150):
            print("not enough milk")
        else:
            print("please enter coins")
            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01
            if(total > 2.5):
                print(f"here is {total-2.5}")
                money+=2.5
                print("here is your latte")
                resources["water"]-=200
                resources["coffee"]-=24
                resources["milk"]-=150
            elif(total == 2.5):
                money += 2.5
                print("here is your latte")
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"]-=150
            else:
                print("not enough money. it has been refunded")
    else:
        if (resources["water"] < 250 and resources["coffee"] < 24 and resources["milk"] < 100):
            print("Not enough water and coffee and milk")
        elif (resources["water"] < 250 and resources["coffee"] < 24):
            print("not enough water and coffee")
        elif (resources["water"] < 250 and resources["milk"] < 100):
            print("not enough water and milk")
        elif (resources["coffee"] < 24 and resources["milk"] < 100):
            print("not enough coffee and milk")
        elif (resources["water"] < 250):
            print("not enough water")
        elif (resources["coffee"] < 24):
            print("not enough coffee")
        elif (resources["milk"] < 100):
            print("not enough milk")
        else:
            print("please enter coins")
            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01
            if (total > 3):
                print(f"here is {total - 3}")
                money += 3
                print("here is your cappuccino")
                resources["water"] -= 250
                resources["coffee"] -= 24
                resources["milk"] -= 100
            elif (total == 3):
                money += 3
                print("here is your cappuccino")
                resources["water"] -= 250
                resources["coffee"] -= 24
                resources["milk"] -= 100
            else:
                print("not enough money. it has been refunded")