from map import Map
from companion import Companion


class Engine():
    """
    """
    def __init__(self):
        self.map = Map()
        self.companion = Companion()
        self.startingRoom = 1
        self.playing = True

    def get_companion(self):
        companionName = self.companion.choose_companion()
        if companionName is None:
            print("You have entered an invalid name or number for a companion. Try again.\n")
            companionName = self.companion.choose_companion()
        return companionName

    def play(self):
        companionName = self.get_companion()
        roomsWithItems, roomsWithMonsters = self.map.setupMap()
        print("You have chosen {} as your companion".format(companionName))
        while self.playing:
            userInput = input("Enter Action: ")
            self.quit(userInput)
            self.help(userInput)

    def quit(self, userInput):
        if userInput.lower() == "quit":
            self.playing = False

    def help(self, userInput):
        if userInput.lower() == "help":
            print("Help selected")
