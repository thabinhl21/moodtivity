from timeline import *
from date import *
from activity import *
from mood import *
import unittest

def create_temline_for_test():
        timeline = Timeline()

        date1 = Date("7/19/2022")
        date2 = Date("7/20/2022")
        date3 = Date("7/21/2022")

        timeline.add_date(date1)
        timeline.add_date(date2)
        timeline.add_date(date3)

        bad = Mood("Bad", 1)
        angry = Mood("Angry", 2)
        good = Mood("Good", 3)

        sleep = Activity("sleep", bad, 120, "Sleep cures all! Why don't you catch some z's?")
        faith = Activity("faith", angry, 5, "Are you spiritual? If so, you might want to consult a higher power")
        vent = Activity("vent", good, 10, "Venting to a loved one can take the edge off. If they will listen of course")
        pet = Activity("pet", bad, 5, "Just 5 minutes with a pet can put a smile on your face")
        drive = Activity("drive", good, 120, "Sleep cures all! Why don't you catch some z's?")
        nature = Activity("nature", angry, 120, "Sleep cures all! Why don't you catch some z's?")
        comedy = Activity("comedy", bad, 120, "Sleep cures all! Why don't you catch some z's?")
        game = Activity("game", angry, 120, "Sleep cures all! Why don't you catch some z's?")
        read = Activity("read", good, 120, "Sleep cures all! Why don't you catch some z's?")
        breathe = Activity("breathe", bad, 120, "Sleep cures all! Why don't you catch some z's?")


        timeline.dateList[0].add_activity(sleep)
        timeline.dateList[0].add_activity(game)
        timeline.dateList[0].add_activity(drive)
        timeline.dateList[0].add_activity(breathe)
        timeline.dateList[0].add_mood(bad)
        timeline.dateList[0].add_mood(angry)
        timeline.dateList[0].add_mood(good)
        
        timeline.dateList[1].add_activity(faith)
        timeline.dateList[1].add_activity(pet)
        timeline.dateList[1].add_activity(read)
        timeline.dateList[1].add_mood(bad)
        timeline.dateList[1].add_mood(angry)
        
        timeline.dateList[2].add_activity(comedy)
        timeline.dateList[2].add_activity(vent)
        timeline.dateList[2].add_activity(sleep)
        timeline.dateList[2].add_mood(bad)
        timeline.dateList[2].add_mood(good)

        return timeline

class TestTimeline(unittest.TestCase):

    def test_create_timeline(self):
        timeline = Timeline()
        self.assertEqual(timeline.get_timeline(), [])

    def test_add_date(self):
        timeline = Timeline()
        date1 = Date("7/19/2022")
        date2 = Date("7/20/2022")
        date3 = Date("7/21/2022")

        timeline.add_date(date1)
        timeline.add_date(date2)
        timeline.add_date(date3)

        self.assertEqual(timeline.get_timeline(), [date1, date2, date3])

    def test_print_list(self):
        timeline = create_temline_for_test()
        timeline.printList()
        
    def test_print_list_by_mood(self):
        timeline = create_temline_for_test()
        moods = ["Angry", "Good"]
        timeline.printListByMood(moods)


if __name__ == "__main__":
    unittest.main()