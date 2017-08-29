import unittest
import gui_skeleton.py

class CorrectFileTest(unittest.TestCase):
    """
    """

    def test_has_right_ui_file_to_build_skeleton(self):
        self.assertEqual('adventureGame.ui', self.qtCreatorFile)
        


if __name__ == '__main__':
    unittest.main(warnings='ignore')