import unittest
from readText import ReadDescriptions
from room import Rooms


class CorrectFileTest(unittest.TestCase):
    """
    """

    def test_can_create_room_dictionary(self):
        roomsDict = Rooms()
        self.assertEqual({
            1: {}, 2: {}, 3: {}, 4: {}, 5: {},
            6: {}, 7: {}, 8: {}, 9: {}, 10: {}},
                         roomsDict.setRoomNumberKeys())

    def test_can_add_items_to_a_room(self):
        roomsDict = Rooms()
        roomsDict.setRoomNumberKeys()
        self.assertEqual({
            1: {'items': []},
            2: {'items': ["eye of newt"]}, 3: {'items': []},
            4: {'items': ["lizard's leg"]},
            5: {'items': []},
            6: {'items': []},
            7: {'items': ["toe of frog"]},
            8: {'items': ["owlet's wing"]},
            9: {'items': []},
            10: {'items': ["cat hair"]}},
                         roomsDict.setRoomObjects())

    def test_can_add_directions_to_a_room(self):
        roomsDict = Rooms()
        roomsDict.setRoomNumberKeys()
        roomsDict.setRoomObjects()
        self.assertEqual({
            1: {'items': [], 'directions': {
                'north': 3, 'east': 6, 'south': 8, 'west': 5}},
            2: {'items': ["eye of newt"], 'directions': {
                'north': None, 'east': 3, 'south': 2, 'west': 2}},
            3: {'items': [], 'directions': {
                'north': None, 'east': 4, 'south': 1, 'west': 2}},
            4: {'items': ["lizard's leg"], 'directions': {
                'north': None, 'east': 6, 'south': 6, 'west': None}},
            5: {'items': [], 'directions': {
                'north': None, 'east': 1, 'south': None, 'west': 7}},
            6: {'items': [], 'directions': {
                'north': 4, 'east': 9, 'south': 8, 'west': 1}},
            7: {'items': ["toe of frog"], 'directions': {
                'north': 2, 'east': None, 'south': None, 'west': 5}},
            8: {'items': ["owlet's wing"], 'directions': {
                'north': None, 'east': 6, 'south': None, 'west': None}},
            9: {'items': [], 'directions': {
                'north': 6, 'east': None, 'south': None, 'west': 10}},
            10: {'items': ["cat hair"], 'directions': {
                'north': None, 'east': 9, 'south': None, 'west': None}}},
                         roomsDict.setRoomDirections())

    def test_can_keep_track_of_visits(self):
        roomsDict = Rooms()
        roomsDict.setRoomNumberKeys()
        roomsDict.setRoomObjects()
        roomsDict.setRoomDirections()
        self.assertEqual({
            1: {'items': [], 'directions': {
                'north': 3, 'east': 6, 'south': 8, 'west': 5},
                'visits': 0},
            2: {'items': ["eye of newt"], 'directions': {
                'north': None, 'east': 3, 'south': 2, 'west': 2},
                'visits': 0},
            3: {'items': [], 'directions': {
                'north': None, 'east': 4, 'south': 1, 'west': 2},
                'visits': 0},
            4: {'items': ["lizard's leg"], 'directions': {
                'north': None, 'east': 6, 'south': 6, 'west': None},
                'visits': 0},
            5: {'items': [], 'directions': {
                'north': None, 'east': 1, 'south': None, 'west': 7},
                'visits': 0},
            6: {'items': [], 'directions': {
                'north': 4, 'east': 9, 'south': 8, 'west': 1},
                'visits': 0},
            7: {'items': ["toe of frog"], 'directions': {
                'north': 2, 'east': None, 'south': None, 'west': 5},
                'visits': 0},
            8: {'items': ["owlet's wing"], 'directions': {
                'north': None, 'east': 6, 'south': None, 'west': None},
                'visits': 0},
            9: {'items': [], 'directions': {
                'north': 6, 'east': None, 'south': None, 'west': 10},
                'visits': 0},
            10: {'items': ["cat hair"], 'directions': {
                'north': None, 'east': 9, 'south': None, 'west': None},
                 'visits': 0}},
                         roomsDict.setRoomVisits())

    def test_can_get_correct_room_descriptons(self):
        # roomsDict = Rooms()
        # roomsDict.setRoomNumberKeys()
        # roomsDict.setRoomObjects()
        # roomsDict.setRoomDirections()
        # print roomsDict.setRoomDescriptions()
        descriptions = ReadDescriptions()
        print descriptions.readFile()

if __name__ == '__main__':
    unittest.main()
