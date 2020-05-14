n = int(input())
list = []
for i in range(n):
    x = input()
    if "insert" in x:
        splited = x.split(" ")
        list.insert(int(splited[1]),int(splited[2]))
    elif "print" in x:
        print(list)
    elif "remove" in x:
        splited = x.split(" ")
        list.remove(int(splited[1]))
    elif "append" in x:
        splited = x.split(" ")
        list.append(int(splited[1]))
    elif "sort" in x :
        list.sort()
    elif "pop" in x :
        list.pop()
    elif "reverse" in x :
        list.reverse()
