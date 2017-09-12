import unittest
from readText import ReadDescriptions
from room import Rooms


class CorrectFileTest(unittest.TestCase):
    """
    """

    def test_can_create_room_dictionary(self):
        roomsDict = Rooms()
        self.assertEqual({1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}}, 
            roomsDict.setRoomNumberKeys())





if __name__ == '__main__':
    unittest.main()