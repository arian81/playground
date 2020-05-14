temp = int(input("how's the whether"))
unit = input("select your unit c or f")
if unit == "f":
    x=(temp-32)*5/9
    print(f"it's {x} centigrad outside")
elif unit == "c":
    y = (temp*9/5)+32
    print(f"it's {y} farenheight outside")

else:
    print("go fuck yourself")
