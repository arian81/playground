import random
list_1 = []
list_2 = []
c = []


for i in range(100):
    list_1.append(random.randint(1,10001))
    list_2.append(random.randint(1,10001))


x = set(list_1)
y = set(list_2)

for i in x:
    for j in y:
        if i == j:
            c.append(i)
        else:
            pass

print(c)
