import date

class Timeline:

    def __init__(self):
        self.dateList = []

    def get_timeline(self):
        return self.dateList

    def add_date(self, date):
        self.dateList.append(date)

    def printList(self):
        for i in range(len(self.dateList)):
            print(self.dateList[i].get_date())
            self.dateList[i].displayActivities()
            self.dateList[i].displayMoods()
            print("")

    def printListInverse(self):
        i = len(self.dateList) - 1
        while i > 0 :
            print(self.dateList[i].get_date())
            self.dateList[i].displayActivities()
            self.dateList[i].displayMoods()
            print("")
            i -= 1

    #print by all type of mood
    def printListByMood(self):
        for i in range(len(self.dateList)):
            print(self.dateList[i].get_date())
            self.dateList[i].displayActivitiesByMood("Angry")
            self.dateList[i].displayActivitiesByMood("Annoyed")
            self.dateList[i].displayActivitiesByMood("Anxious")
            self.dateList[i].displayActivitiesByMood("Bad Day")
            self.dateList[i].displayActivitiesByMood("Bored")
            self.dateList[i].displayActivitiesByMood("Stressed")
            self.dateList[i].displayActivitiesByMood("Tired")

    #print by a list of choiced mood, pass in a list of mood name
    #ex. moods = ["Angry", "Tired", "Streesed"]
    def printListByMood(self, moods):
        for i in range(len(self.dateList)):
            print(self.dateList[i].get_date())
            for j in range(len(moods)):
                self.dateList[i].displayActivitiesByMood(moods[j])
            