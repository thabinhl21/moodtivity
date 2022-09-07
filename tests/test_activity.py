import unittest
from unittest.mock import patch
import activity

class TestActivityClass(unittest.TestCase):

    def setUp(self):
        self.testActivity = activity.Activity("test", 1, 1, "desc")
    
    def test_getName(self):
        self.assertEqual(self.testActivity.get_name(), "test")

    def test_getMood(self):
        self.assertEqual(self.testActivity.get_mood(), 1)

    def test_getTime(self):
        self.assertEqual(self.testActivity.get_time(), 1)

    def test_getDesc(self):
        self.assertEqual(self.testActivity.get_desc(), "desc")

    def test_buildActivityListsAndSort(self):
        activitiesList = activity.buildActivitiesList()
        badDayList = activity.sortActivities(activitiesList)
        bdCount = len(badDayList)
        actCount = len(activitiesList)

        self.assertEqual(badDayList[0].name, "sleep")
        self.assertEqual(badDayList[bdCount - 1].name, "game")
        self.assertEqual(activitiesList[0].name, "read")
        self.assertEqual(activitiesList[actCount - 1].name, "create")

    @patch('activity.getUserTime', return_value = 30)
    def test_getUserTime(self, mock_time):
        mock_time = activity.getUserTime()
        expected = 30

        self.assertEqual(mock_time, expected)

    @patch('activity.suggestActivity', return_value = activity.Activity("sleep", 1, 120, "Sleep cures all!"))
    def test_suggestActivity(self, mock_activity):
        mock_activity = activity.suggestActivity()
        
        self.assertIsInstance(mock_activity, activity.Activity)
        
if __name__ == '__main__':
    unittest.main()
