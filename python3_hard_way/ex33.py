i = 0
numbers = []

def while_loop(x,y):
    global i
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i +=y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


print("The numbers: ")

while_loop(12,2)
