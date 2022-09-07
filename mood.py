import json

class Mood:

    #Defines the mood object with a string (name).
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __repr__(self):
        return f'{self.name}'

    def get_name(self):
        return self.name
    
    def get_num(self):
        return self.num

    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return Mood(**json_dict)

def buildMoodLists():
    moodsList = []
    with open('moods.json', 'r') as json_file:
        moods = json.loads(json_file.read())
        for m in moods:
            moodsList.append(Mood(**m))

    return moodsList   

#List of specific moods

def sortMoods(moodsList):
    specificMoods = []
    
    for m in moodsList:
        if m.get_num() == "2":
            specificMoods.append(m)

    for i in range(5):
        moodsList.pop(1)

    moodsList.insert(1, specificMoods)

#Gets the user's mood and validates input
def getUserMood():
    while True:
        try:
            mood = int(input("How are you today? 1 = Having a bad day; 2 = Not great; 3 = Good/Fine just bored\n"))
        except ValueError:
            print("You must input an integer")
            continue
        
        if mood == 1 or mood == 2 or mood == 3:
            break
        else:
            print("You must select option 1, 2, or 3")
            continue

    return mood
