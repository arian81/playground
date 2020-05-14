import string
alphabet = string.ascii_lowercase
x = input()
p = set(x)
t = []
total = 0
for i in p:
    t.append(i)
for i in t:
    score1 = x.count(i)
    score2 = (alphabet.index(i)+1)
    mult = score1 * score2
    total += mult
print(total)
