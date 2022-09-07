from date import *
from activity import *
from mood import *
import unittest

def create_date_for_test():
        date = Date("7/19/2022")

        bad = Mood("Bad", 1)
        angry = Mood("Angry", 2)
        good = Mood("Good", 3)

        sleep = Activity("sleep", bad, 120, "Sleep cures all! Why don't you catch some z's?")
        faith = Activity("faith", angry, 5, "Are you spiritual? If so, you might want to consult a higher power")
        vent = Activity("vent", good, 10, "Venting to a loved one can take the edge off. If they will listen of course")
        
        date.add_activity(sleep)
        date.add_activity(faith)
        date.add_activity(vent)

        date.add_mood(bad)
        date.add_mood(angry)
        date.add_mood(good)

        return date

class TestDate(unittest.TestCase):

    def test_create_date(self):
        date = Date("7/19/2022")
        self.assertEqual(date.get_date(), "7/19/2022")

    def test_get_activity(self):
        date = Date("7/19/2022")
        self.assertEqual(date.get_activity(), [])

    def test_add_activity(self):
        date = Date("7/19/2022")

        bad = Mood("Bad", 1)
        angry = Mood("Angry", 2)
        good = Mood("Good", 3)

        sleep = Activity("sleep", bad, 120, "Sleep cures all! Why don't you catch some z's?")
        faith = Activity("faith", angry, 5, "Are you spiritual? If so, you might want to consult a higher power")
        vent = Activity("vent", good, 10, "Venting to a loved one can take the edge off. If they will listen of course")
        
        date.add_activity(sleep)
        date.add_activity(faith)
        date.add_activity(vent)

        self.assertEqual(date.get_activity(), [sleep, faith, vent])

    def test_display_activities(self):
        date = create_date_for_test()

        output = "sleep\nfaith\nvent"
        date.displayActivities()
        print(output)

    def test_get_mood(self):
        date = Date("7/19/2022")
        self.assertEqual(date.get_mood(), [])

    def test_add_mood(self):
        date = Date("7/19/2022")

        bad = Mood("Bad", 1)
        angry = Mood("Angry", 2)
        good = Mood("Good", 3)

        date.add_mood(bad)
        date.add_mood(angry)
        date.add_mood(good)

        self.assertEqual(date.get_mood(), [bad, angry, good])

    def test_display_moods(self):
        date = create_date_for_test()

        output = "bad\nangry\ngood"
        date.displayMoods()
        print(output)
        
    def test_display_activities_by_mood(self):
        date = create_date_for_test()

        date.displayActivitiesByMood("Good")
        print("vent")

if __name__ == "__main__":
    unittest.main()