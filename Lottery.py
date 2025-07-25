import random
lotteryAnswer = str(random.randint(1,50))
guess = 0
while guess != lotteryAnswer:
    guess = input("What is your guess?")
    if guess == lotteryAnswer:
        print("Jackpot!!")
    elif guess == "hint":
        print("No hints! Now I'm changing the number")
        lotteryAnswer = str(random.randint(1,50))
    elif guess == "hint please":
        print(lotteryAnswer)
    else: 
        print("Try again")
