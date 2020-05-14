class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def evil(self):
        print(evil_morty)
happy_bday = song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = song(["They rally around tha family",
                        "With pockets full of shells"])

goodbye_moonmen = song(["The world can be one together",
                        "Cosmos without hatred",
                        "Stars like diamonds in your eyes",
                        "The ground can be space, space, space space, space",
                        "With feet matching toward the peaceful sky",
                        "All the moonmen want things their way",
                        "But we make sure they see the sun",
                        "Goodbye moonmen",
                        "Yeah we say goodbye moonmen",
                        "Goodbye moonman",
                        "Goodbye moonman",
                        "Oh goodbye",
                        "Cosmos with hatred",
                        "Diamonds, stars of cosmic light",
                        "Quaysare shine through endless nights",
                        "And everything is one in the beauty",
                        "And now we say goodbye moonmen",
                        "We say goodbye moonmen",
                        "Goodbye moonman",
                        "Goodbye moonman",
                        "Oh goodbye"])

evil_morty = """Maybe again
                He will be alone
                Guess we're equally damaged
                Find your name
                Do it all the same equally
                Signal when you can't breathe no more

                Say you were me
                Then you could see the view
                You'll know we are equally damaged
                Don't be a fool, make it easier
                You'll learn to say when
                Signal if you can't
                Say, "no more"

                Don't cross your finger
                Sundays will never change
                They keep on coming
                You'll be a freak
                And I'll keep you company"""

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

goodbye_moonmen.sing_me_a_song()

x = song(evil_morty)
x.evil()
