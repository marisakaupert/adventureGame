from map import Map


class Engine():
    """
    """
    def __init__(self, rooms_map):
        self.rooms_map = Map(1)

    def play(self):
        start = self.rooms_map.opening_room
        return start

    def help(self):
        pass

    def quit(self):
        pass
