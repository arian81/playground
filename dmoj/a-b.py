n = int(input())
p = []
for i in range(n):
    n = input()
    n = n.split(" ")
    a = int(n[0])
    b = int(n[1])
    result = a-b
    p.append(result)

for i in p:
    print(i)
