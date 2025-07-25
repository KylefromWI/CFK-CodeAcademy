done = False

lemonadeCost = 30.00
breadCost = 1.00

userMoney = 26000000000

while not done:

    print("======================================")
    print(" WELCOME TO THE DIGITAL LEMONADE STAND")
    print("======================================")
    print()

    choice = input("What would you like to buy? or are you done? lemonade or bread are good choices")
    if choice == "lemonade":
        userMoney -= lemonadeCost
        print("Thank you, here you go")
    elif choice == "bread":
        userMoney -= breadCost
        print("Thank you, here is your bread")

    elif choice == "done":
        done = True
        print("Thank you, good bye")
    else:
        cash = str(userMoney)
        print("You have $", cash, "left")
