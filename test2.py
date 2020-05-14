def swap_case(s):
    k=''
    for i in range(len(s)):
        if s[i].islower():
            k+=s[i].upper()
        elif s[i].isupper():
            k+=s[i].lower()
        else:
            k+=s[i]
    print(k)
swap_case("Hello World")
