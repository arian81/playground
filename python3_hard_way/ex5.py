my_name = 'Zed A. Shaw'
my_age = 35 #not a  if lie
my_height = 74 # inches
my_weight = 180 # Ibs
my_eyes = "blue"
my_teeth = 'white'
my_hair = 'brown'

height_converter=round(my_height*2.54)
weight_converter=round(my_weight*0.453592)


print(f"Let's talk about {my_name}")
print(f"He's {height_converter} inches tall.")
print(f"He's {weight_converter} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee")
# this line is tricky, try to get it exactly right
total = my_age + height_converter + weight_converter
print(f"If I add {my_age}, {height_converter}, I get {total}.")
