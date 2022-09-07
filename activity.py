import json

class Activity:
    
    #Assigns each activity a name, a time duration in mins, and a description. Name and description are strings. Time is an integer.
    def __init__(self, name, mood, time, desc):
        self.name = name
        self.mood = mood
        self.time = time
        self.desc = desc

    def __repr__(self):
        return f'{self.name}'

    def get_name(self):
        return self.name

    def get_mood(self):
        return self.mood

    def get_time(self):
        return self.time

    def get_desc(self):
        return self.desc

    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return Activity(**json_dict)     

#Reading activities from json file and storing them in a list
def buildActivitiesList():
    activitiesList = []
    with open('activities.json', 'r') as json_file:
        activities = json.loads(json_file.read())
        for a in activities:
            activitiesList.append(Activity(**a))

    return activitiesList        

#Building Activity List
def sortActivities(list):
    badDayList = []
    
    for a in list:
        if a.get_mood() == "1":
            badDayList.append(a)

    for i in range(8):
        list.pop(0)

    return badDayList
           


#Gets the user's time constraint and validates input
def getUserTime():
    while True:
        try:
            time = int(input("How much time do you have available? Answer in minutes\n"))
        except ValueError:
            print("You must input an integer")
            continue
        
        if time > 0:
            break
        else:
            print("You must input a value greater than 0")
            continue

    return time

#Recommend an activity based on a given list and time constraint. Returns the activity object or None if no activity is selected.
def suggestActivity(activityList, userTime):
    newList = []

    for obj in activityList:
        if userTime >= int(obj.get_time()):
            newList.append(obj)

    print(newList)
    for x in newList:
        print(x.get_desc() + "\n")
        
        while True:
            try:
                decision = int(input("Would you like to do this activity? 1 = yes, 2 = no\n"))
            except ValueError:
                print("You must input an integer")
                continue
            
            if decision < 1 or decision > 2:
                print("You must input either 1 or 2")
                continue
            else:
                break

        if decision == 1:
            return x.get_name()
        else:
            continue

    return
