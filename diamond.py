num_list = []
def diamond(x):
    for i in range(len(x)):
        print(" "*(len(x)-i)+(i*2+1)*x[i])
        num_list.append(i*2+1)
    num_list.reverse()
    for i in range(len(x)):
        print(" "*(i+1)+num_list[i]*x[i])
diamond(10)