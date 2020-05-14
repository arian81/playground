def count_substring(string, sub_string):
    p=0
    x = list(sub_string)
    lst = []
    str = list(string)
    for i in str:
        if i in sub_string:
            lst.append(i)
        else:
            pass
    
    
    for i in range(len(lst)):
        if lst[0:3]==x:
            p+=1
            del(lst[0])
        else:
            del(lst[0])        

    
    return lst
print(count_substring("ThIsisCoNfUsInG","is"))