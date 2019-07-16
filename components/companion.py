


class Companion(object):
    """
    """
    def __init__(self):
        self.companions = dict({1: "Flower", 2: "Momo the Mouse", 3: "Mayor Manana"})

    def get_companion_input(self):
        companionNames = list(self.companions.values())
        print("You are going on a quest!")
        print("Your options are:")
        print("1. {}- Stats: +0 Strength, +0 Relationships, +5 Charisma.".format(companionNames[0]))
        print("2. {}- Stats: +5 Strength, +0 Relationships, +0 Charisma".format(companionNames[1]))
        print("3. {}- Stat: +0 Strength, +5 Relationships, +0 Charisma".format(companionNames[2]))
        companionChoice = input("Enter the companion's number. Who do you choose? ")
        return companionChoice

    def choose_companion(self):
        companionChoice = self.get_companion_input()
        if companionChoice.isdigit():
            if int(companionChoice) in self.companions:
                companion = self.companions[int(companionChoice)]
            else:
                companion = None
        else:
            companion = None

        return companion
