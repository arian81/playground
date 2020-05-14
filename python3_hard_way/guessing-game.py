import random

number = random.randint(1,9)
win = False
choice = 0
counter = 0
print("Guess what number do i have in my mind?")

while choice != number:
    choice = int(input("> "))

    if choice == number:
        print(f"Well done. You guessed right and you've done it in {counter} tries")
    elif number > choice:
        print("You need to aim higher")
        counter +=1
    elif choice > number:
        print("You're flying too high")
        counter +=1
    else:
        print("not in the range")
