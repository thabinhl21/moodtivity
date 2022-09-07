import activity
import mood
from data import *

class FindActivity:

    def __init__(self):
        pass

    def rec_activity(self):
        activityList = activity.buildActivitiesList()
        badDayList = activity.sortActivities(activityList)

        moodCategories = mood.buildMoodLists()
        specificMoods = mood.sortMoods(moodCategories)

        #Prompt the user and validate input
        userInput = mood.getUserMood()

        #Set the activityList and userMood variables based on the previous user input
        if userInput == 1:
            userMood = moodCategories[0]

        #Get the user's specific mood
        elif userInput == 2:
            while True:
                try:
                    newInput = int(input("What's wrong? 1 = Stressed, 2 = Anxious, 3 = Angry, 4 = Annoyed, 5 = Tired\n"))
                except ValueError:
                    print("You must input an integer")
                    continue
                
                if newInput < 1 or newInput > 5:
                    print("You must select an option from 1-5")
                    continue
                else:
                    break
            
            tempList = moodCategories[1]
            userMood = tempList[newInput - 1]
            del tempList

        else:
            userMood = moodCategories[2]

        #Prompt the user and validate input
        userTime = activity.getUserTime()

        #Suggest activities for the user until one is selected
        if userMood.get_num() == "1":
            userActivity = activity.suggestActivity(badDayList, userTime)
            # active = Data("activityTable")
            # active.create_activity_table()
            # active.insert_activity("", "", userActivity)
            print("Great!")
            # print(userActivity)
            return userActivity
        else:
            userActivity = activity.suggestActivity(activityList, userTime)

        if userActivity == None:
            print("No activity was selected. Maybe next time!")


