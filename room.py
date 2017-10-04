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
        for i in self.roomInformation.keys():
            self.roomInformation[i]['items'] = []
            if i == 2:
                self.roomInformation[i]['items'] = ["eye of newt"]
            if i == 4:
                self.roomInformation[i]['items'] = ["lizard's leg"]
            if i == 7:
                self.roomInformation[i]['items'] = ["toe of frog"]
            if i == 8:
                self.roomInformation[i]['items'] = ["owlet's wing"]
            if i == 10:
                self.roomInformation[i]['items'] = ["cat hair"]

        return self.roomInformation

    def setRoomDirections(self):
        for i in self.roomInformation.keys():
            self.roomInformation[i]['directions'] = {}
            if i == 1:
                self.roomInformation[i]['directions'] = {
                    'north': 3, 'east': 6, 'south': 8, 'west': 5}
            if i == 2:
                self.roomInformation[i]['directions'] = {
                    'north': None, 'east': 3, 'south': 2, 'west': 2}
            if i == 3:
                self.roomInformation[i]['directions'] = {
                    'north': None, 'east': 4, 'south': 1, 'west': 2}
            if i == 4:
                self.roomInformation[i]['directions'] = {
                    'north': None, 'east': 6, 'south': 6, 'west': None}
            if i == 5:
                self.roomInformation[i]['directions'] = {
                    'north': None, 'east': 1, 'south': None, 'west': 7}
            if i == 6:
                self.roomInformation[i]['directions'] = {
                    'north': 4, 'east': 9, 'south': 8, 'west': 1}
            if i == 7:
                self.roomInformation[i]['directions'] = {
                    'north': 2, 'east': None, 'south': None, 'west': 5}
            if i == 8:
                self.roomInformation[i]['directions'] = {
                    'north': None, 'east': 6, 'south': None, 'west': None}
            if i == 9:
                self.roomInformation[i]['directions'] = {
                    'north': 6, 'east': None, 'south': None, 'west': 10}
            if i == 10:
                self.roomInformation[i]['directions'] = {
                    'north': None, 'east': 9, 'south': None, 'west': None}

        return self.roomInformation

    def setRoomVisits(self):
        for i in self.roomInformation.keys():
            self.roomInformation[i]['visits'] = 0

        return self.roomInformation

    def setRoom1Descriptions(self):
        descriptions = ReadDescriptions()
        x = descriptions.readFile()
        for i in x:
            if i.startswith('firstVisit'):
                pass
            elif i.startswith('otherVisits'):
                pass
            elif i.startswith('winningText'):
                pass
            elif i.startswith('preAction'):
                pass
            elif i.startswith('postAction'):
                pass
            else:
                print i
