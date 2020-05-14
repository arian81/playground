text = input()
for i in text:
    if i == "-":
        s = text.index("-")
        g = i.upper()
        text.replace(i,g)
        text.pop(i)

    else:
        pass
print(text)
