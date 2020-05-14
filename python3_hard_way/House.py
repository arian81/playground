from PIL import Image
import tkinter
from tkinter import messagebox
from sys import exit
timer = range(1,100)

inventory = []
doors = ["wooden",'metallic','red','black','golden','gray']
def game_over():
    img = Image.open("game_over.jpg")
    img.show()
    print("1.try again                 2.exit")
    choice = input(" >")
    if choice == '1':
        start()
    elif choice == '2':
        exit(0)
def abyss():
    print("Just as you step inside there is nothing beneth you")
    print("The rush of the moment take you by surprise ")
    print("It dosen't matter because your couln't do anything anyway")
    print("Have fun falling for every")
    falling = True
    for i in timer:
        print("Aaaaahhhhh")
    print("Still here? You can go back to the begining")
    start()

def dungeon():
    if not "sword" in inventory:
        print('Welcome to dungeon')
        print("you're going to have a lot of fun with kevin (My beloved dragon)")
        print("do you rather get barbecued by kevin or eaten raw?")
        choice = input(" >")
        if "barbecue" in choice:
            print("what a delicious smell. yam yam!")
            game_over()
        elif "raw" in choice:
            print("why? do you want kevin to get human poisening?")
            game_over()
        else:
            print("that's not an option")
    elif sword in inventory:
        print("you have sword you can kill the dragon")
        choice = input(" >")
        if "kill" in choice:
            print("you're imortal now have fun")
            end()
        elif "back" in choice:
            hallway()
def freezer():
    print("ha ha you're in the freezer")
    print("we store meat for kevin in here")
    print("you're going to freeze to death and be ready for as the kevin's next meal")
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Achivment", "Stupidest death Achivment unlocked")
    game_over()

def room_1():
    print('You open the door')
    print("There is absolute darkness on the other side")
    print("you can't do anything unless you bring some sort of light")
    light = False
    secret = input("> ")
    if "flashlight" in secret:
        give_flashlight()
    else:
        print("incorrect code")
        room_1()
    if "flashlight" in inventory:
        print("you can now see what's in the room")
        print("there is a desk in the room. what do you do?")
        print("1.open the drawer \n 2.go back to the hallway")
        choice = input(" >")
        if choice == "1":
            print("you find a key")
            inventory.append("key")
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('Item added','key added')
            hallway()
        elif choice == '2':
            print("you're back in the hallway")
            hallway()
    else:
        print("you can't do anything")

def room_2():
    print('You open the door')
    print("there's a desk with a plate of delicious looking food")
    print("what do you do?")
    print("1.yummm eat the food \n 2.it could be poisend go back to hallway")
    choice = input(' >')
    if choice == '1':
        print("the food is poisend. you're dead")
        game_over()
    elif choice == '2':
        hallway()
    else:
        print("you should enter a number")

def room_3():

    print("You open the door")
    print("on your left there is a huge metallic looking door")
    print("in the middle of room there's a shelf")
    print("what do you do?")
    print("1.check the door \n 2.check the shelf \n 3.go back to hallway")
    choice = input(" >")
    if choice == '1' and not "key" in inventory:
        print("you need a key to proceed")
        room_3()
    elif choice == '1' and "key" in inventory:
        print("you unlock the door and go inside")
        down()
    elif choice == '2':
        print("there is a sword inside")
        inventory.append("sword")
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("item added","sword added")
        room_3()
    elif choice == '3':
        hallway()
    else:
        print("you should enter a number")

def show_inventory():
    print(*inventory, sep = '     ')

def down():
    print("behind the door is a long downhill way with a very dim lighting")
    print("at the end of the hill there are three doors and a gothic looking man is waiting for you")
    print("the man says two of the doors leads to infinite wealth and one to a gruesome death")
    print("you can ask me one question about what a door leads to and i answer in yes or no")
    print("but here's the twist if the door that you're asking me about leads to wealth i answer truthfully and if it leads to death i answer randomly")
    answer = input(" >")
    if "kill" in answer:
        print("you're a smart one you take the fortune and live happily ever after")
        end()
    else:
        game_over()

def start():
    print("you heard about this mystrious house at the cul de sac")
    print("you're too curious to let it go so you go there to investigate it")
    print("the house is in this weird circular shape")
    print("inside you find a circular hallway with a lot of doors")
    print("which door do you choose?")
    print(*doors, sep = '\n')
    choice = input(" >")
    if choice == "wooden":
        abyss()
    elif choice == 'metallic':
        freezer()
    elif choice == 'red':
        dungeon()
    elif choice == 'black':
        room_3()
    elif choice == 'golden':
        room_2()
    elif choice == 'gray':
        room_1()
    else:
        print("you're too dumb to be in this house")
        exit(0)
def give_flashlight():
    inventory.append("flashlight")
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo('Item added','flash light added')
def end():
    print("i hope you had fun ")
    print("the  game is now finished")
    img = Image.open("the_end.jpg")
    img.show()

def hallway():
    print("You're back in the hallway")
    print(*doors, sep = '\n')
    choice = input(" >")
    if choice == "wooden":
        abyss()
    elif choice == 'metallic':
        freezer()
    elif choice == 'red':
        dungeon()
    elif choice == 'black':
        room_3()
    elif choice == 'golden':
        room_2()
    elif choice == 'gray':
        room_1()
    else:
        print("you're too dumb to be in this house")
        exit(0)
root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("A message from the programmer",'you need to examine the code in order to proceed through game \n dont forget about the source code ;)')
start()
