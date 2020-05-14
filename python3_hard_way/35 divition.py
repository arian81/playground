start = int(input("gimme start point"))
end = int(input("gimme end point"))
range_1 = range(start , end)
x = []

for i in range(start,end):
    if i%35 == 0:
        print(f'{i} is right')
    #else:
        #print(f'{i} is wrong')

print(range_1)
