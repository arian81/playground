#t = input()
x = 1
seq = []
xyz = []

def form(p):
    for i in range(1,p+1):
        seq.append(x*(2**(i-1)))

def valid():
    g = 0
    for i in range(len(seq)):
        if g == n:
            l = True
            break
        else:
            g+=seq[i]

n = int(input())
while x < n :
    l = False
    form(n)
    valid()
    if l == True:
        xyz.append(x)
        seq.clear()
    elif l == False:
        x+=1
        seq.clear()
print(seq)
print(xyz)
