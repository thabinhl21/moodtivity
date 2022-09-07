import unittest
from unittest.mock import patch
import mood

class TestMoodClass(unittest.TestCase):

    def setUp(self):
        self.testMood = mood.Mood("test", 1)
        
    def test_getName(self):
        self.assertEqual(self.testMood.get_name(), "test")

    def test_getNum(self):
        self.assertEqual(self.testMood.get_num(), 1)

    @patch('mood.getUserMood', return_value = 1)
    def test_getUserMoodBadDay(self, mock_bad_day):
        mock_bad_day = mood.getUserMood()
        expected = 1

        self.assertEqual(mock_bad_day, expected)

    @patch('mood.getUserMood', return_value = 2)
    def test_getUserMoodNotGreat(self, mock_not_great):
        mock_not_great = mood.getUserMood()
        expected = 2

        self.assertEqual(mock_not_great, expected)

    @patch('mood.getUserMood', return_value = 3)
    def test_getUserMoodFine(self, mock_fine):
        mock_fine = mood.getUserMood()
        expected = 3

        self.assertEqual(mock_fine, expected)

    def test_buildMoodListsAndSort(self):
        moodsList = mood.buildMoodLists()
        mood.sortMoods(moodsList)

        self.assertEqual(moodsList[0].name, "Bad Day")
        self.assertIsInstance(moodsList[1], list)
        self.assertEqual(moodsList[2].name, "Good/Bored")

if __name__ == '__main__':
    unittest.main()
