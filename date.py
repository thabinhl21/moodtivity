import activity
import mood

class Date:

    def __init__(self, date):
        self.date = date
        self.oneday_activities = []
        self.oneday_moods = []

    def get_date(self):
        return self.date

    def get_activity(self):
        return self.oneday_activities

    def add_activity(self, activity):
        self.oneday_activities.append(activity)

    def displayActivities(self):
        print("List of activities in oneday")
        for i in range(len(self.oneday_activities)):
            print(self.oneday_activities[i].get_name())


    #Display the activities by specific mood, mood is string
    def displayActivitiesByMood(self, mood):
        print(mood,"activities in oneday")
        for i in range(len(self.oneday_activities)):
            if(self.oneday_activities[i].get_mood().get_name() == mood):
                print(self.oneday_activities[i].get_name())
        
    def get_mood(self):
        return self.oneday_moods
    
    def add_mood(self, mood):
        self.oneday_moods.append(mood)

    def displayMoods(self):
        print("List of mood in oneday")
        for i in range(len(self.oneday_moods)):
            print(self.oneday_moods[i].get_name())