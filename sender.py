import schedule
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def job():
    keyboard.type("Welcome to the world my little one")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("you thought I'm gonna miss this huh?")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("I'm a progarmmer and I'll find a way to do what I want so here I am made it to your birthtime ")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("Happy birthday and I love you so much see you in something like 6 hours")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("I'm too lazy to figure out emojies so a lot of kisses and hugs")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def job2():
    keyboard.type("I really had fun making this script so I thought let's have more fun with it")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("I hope you had a good day and if somethings wrong then just wake me up it's ok I can help you ")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type("see you soon . lot's of kisses")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    exit()

schedule.every().day.at("4:30").do(job)
schedule.every().day.at("8:00").do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)
