from readText import ReadDescriptions

class Rooms():
    """ The state of the rooms in the game
    """
    def __init__(self):
        self.roomInformation = {}

    def setRoomNumberKeys(self):

        for i in xrange(1, 11):
            self.roomInformation[i] = {}

        return self.roomInformation

    def setRoomObjects(self):
        pass







