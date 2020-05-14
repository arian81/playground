
counter = 0

def correct():
    print("You got 1 point")
    global counter
    counter +=1
def incorrect():
    print("Your answer is incorrect")


print("""Gimme an answer to this math quesions
if you get less than 3 points at the end you're screwed""")

print("First quesion:")
print("Solve 40x - 5y + 35 = 0 for y.")
print("""1. y = 9x + 5
2. y  = -5x + 5
3. y = -9x - 5
4. y = 7x - 8
5. None of the above """)

answer_1 = input(" >")

if answer_1 == "5":
    correct()
else:
    incorrect()
print("Second question:")
print("One positive number is 8 times another positive number. The difference between the two numbers is 35. Find the two numbers. ")
print("""
1. 5, 39
2. 32, 4
3. 6, 48
4. 42, 4 """)

answer_2 = input("> ")

if answer_2 == "1":
    correct()
else:
    incorrect()

print("Third quesion:")
print("Solve:  x**2-7x+12")
print("""
1. 3
2. 4
3. -3
4. 1,2 """)

answer_3 = input("> ")

if answer_3 == "4":
    correct()
else:
    incorrect()

print("Fourth quesion:")
print("Factor:  16x**10 y**3 + 24x**7 y**5")
print("""
8x7y3(2x3 + 3y2)
8x7y3(2x3 - 3y2)
8x3y7(2x-3 + 3y2)
8x7y3(-2x3 + 3y-2)
None of the above """)

answer_4 = input("> ")

if answer_4 == "1":
     correct()
else:
    incorrect()

print(f"You got {counter} in total")

if counter < 3:
    print("get out of my school")
else:
    print("Good job")
