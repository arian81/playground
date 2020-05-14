k = int(input("inter your number"))
x = 1
seq = []
def form(p):
    for i in range(1,p+1):
        seq.append(x*(2**(i-1)))

def valid():
    g = 0
    for i in range(len(seq)):
        l = False
        if g == k:
            l = True
            return l
            exit()
        else:
            g+=seq[i]

form(10)
valid()
