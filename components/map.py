import random

class Map(object):
    """
    """
    def __init__(self):
        self.start_room = 1

    def set_room_with_items(self):
        self.roomWithItems = set()

        count = 0
        while count < 5:
            count = self.randomize_room(count, self.roomWithItems)

        return self.roomWithItems

    def randomize_room(self, count, roomSet):
        for itemNum in range(5):
            roomNum = random.randint(2, 10)
            if roomNum not in roomSet:
                roomSet.add(roomNum)
                count += 1
                return count

    def set_rooms_with_monsters(self):
        self.roomsWithMonsters = set()

        count = 0
        while count < 4:
            count = self.randomize_room(count, self.roomsWithMonsters)

        return self.roomsWithMonsters


    def setupMap(self):
        return self.set_room_with_items(), self.set_rooms_with_monsters()

    def get_current_room(self):
        pass

