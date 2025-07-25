import time

#CREATE VARIABLES

done = False
lemonadeCost = 30.00 #lemonade costs a lot in this world
breadCost = 1.00
userMoney = 260 #user has a lot of cash

#Creates a function that prints how much money the user has
def printMoney():
    cash = str(userMoney)
    print("You have $", cash, "left")
    time.sleep(2)

# Main loop
while not done:

    print("======================================")
    print(" WELCOME TO THE DIGITAL LEMONADE STAND")
    print("======================================")
    print()

    choice = input("What would you like to buy? or are you done? lemonade or bread are good choices  ")
    if choice == "lemonade":
        userMoney -= lemonadeCost
        print("Thank you, here you go")
        printMoney()
    elif choice == "bread":
        userMoney -= breadCost
        print("Thank you, here is your bread")
        printMoney()
    elif choice == "done":
        done = True
        print("Thank you, good bye")
        printMoney()
    else:
        print("I don't understand. You can buy lemonade, bread, or you can be done")

print("Another satisifed customer!!")
