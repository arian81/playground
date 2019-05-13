import random
import string
from random import shuffle
import tkinter
from tkinter import messagebox
import qrcode
from PIL import Image
struct= []

def numgen():
    for i in range(0,digit):
        a = random.randint(0,9)
        struct.append(a)
    global b
    if choice == "1" or "2":
        b =''.join(str(i) for i in struct)
    else:
        pass
def lettergen():
    for i in range(0,digit):
        x = random.choice(string.ascii_letters)
        struct.append(x)
    global c
    if choice == "1" or "2":
        c = ''.join(str(i) for i in struct)
    else:
        pass
def mixgen():
    numgen()
    lettergen()
    shuffle(struct)
    if len(struct)>digit:
        while len(struct)>digit:
            struct.pop(-1)
    global d
    d = ''.join(str(i) for i in struct)
def message_output(sa):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("your generated password",f"here's your password: \n {sa}")
def file_output(sa):
    f=open("output.txt",'w')
    f.write(f"your password is :\n {sa}")
    f.close()
    print("All done check your folder")
def script_output(sa):
    print("Here's your password")
    print(sa)
    input(" ")
def qrcode_output(sa):
    img = qrcode.make(f"{sa}")
    img.show()
def output_chooser(sa):
    if output == '1':
        message_output(sa)
    elif output == '2':
        file_output(sa)
    elif output == '3':
        script_output(sa)
    elif output == '4':
        qrcode_output(sa)
    else:
        print("wrong input")
print("Hello, Welcome to passpy password generator")
print("choose an option: ")
print(" 1.week \n 2.medium \n 3.strong \n 4.insane")
choice = input("> ")
print("and how do you want your output?")
print(" 1.message \n 2.plain text file \n 3.inside the script \n 4.qrcode :) ")
output = input(" >")
if choice == '1' or choice == '2' or choice == '3':
    print("how many digts do you want your password to be?")
    digit = int(input("> "))
    if choice == "1":
        numgen()
        output_chooser(b)
    elif choice == "2":
        lettergen()
        output_chooser(c)
    elif choice == "3":
        mixgen()
        output_chooser(d)
elif choice == '4':
    print("Well You've asked for it")
    digit = 256
    mixgen()
    output_chooser(d)
else :
    print("wrong input. please try again")
