import unittest
from ..adventureGame.engine import Engine


class RoomInformationTest(unittest.TestCase):
    """
    """
    def test_can_start_in_room_1(self):
        start = Engine(rooms_map=1)
        return start

if __name__ == '__main__':
    unittest.main()
