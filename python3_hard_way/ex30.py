people = 30
cars = 40
trucks = 15


if cars > people:
    print("we should take the cars")
elif cars < people:
    print("We should take a cab")
else:
    print("We don't decide")

if trucks>cars:
    print("That's too much trucks")
elif trucks < cars:
    print("Mabey we could take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then")
