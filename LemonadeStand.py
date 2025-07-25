import time

#CREATE VARIABLES

done = False
lemonadeCost = 30.00 #lemonade costs a lot in this world
breadCost = 1.00
beanCost = 2.00
userMoney = 260 #user has a lot of cash
toeCost = 50.0
kidneyCost = 100.00

#Creates a function that prints how much money the user has
def printMoney():
    cash = str(userMoney)
    print("You have $", cash, "left")
    time.sleep(2)


def secretMenu():
    
    print("======================================")
    print(" YOUVE REACHED THE SECRET MENU")
    print("======================================")
    print()

    choice = input("You've reached the secret menu! Would you like a toe or a kidney?")
    if choice == "a toe":
        userMoney -= toeCost
        print("Enjoy that toe, good luck")
        printMoney()
    elif choice == "a kidney":
        userMoney -= kidneyCost
        print("Get well soon")
        printMoney()

# Main loop
while not done:

    print("======================================")
    print(" WELCOME TO THE DIGITAL LEMONADE STAND")
    print("======================================")
    print()

    choice = input("What would you like to buy? or are you done? lemonade, bean, or bread are good choices  ")
    if choice == "lemonade":
        userMoney -= lemonadeCost
        print("Thank you, here you go")
        printMoney()
    elif choice == "bread":
        userMoney -= breadCost
        print("Thank you, here is your bread")
        printMoney()
    elif choice == "bean":
        userMoney -= beanCost
        print("Thank you, here is your bread")
        printMoney()
    elif choice == "secret menu":
        secretMenu()sec
    elif choice == "done":
        done = True
        print("Thank you, good bye")
        printMoney()
    else:
        print("I don't understand. You can buy lemonade, bread, bean, or you can be done")

print("Another satisifed customer!!")
