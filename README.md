[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8066026&assignment_repo_type=AssignmentRepo)
# Moodtivity
 
Authors: [Binh Le](https://github.com/thabinhl21), [Garrett Greenup](https://github.com/garrettgreenup), [Yufeng Chen](https://github.com/Ychen1041), [Claudia Pascual](https://github.com/cpascx)
 

## Project Description
 * For our project, we decided to build an activity recommender based on an individual's mood and the amount of free time that they have. 
 * We are used [Python](https://www.python.org/) for our backend and [TKinter](https://docs.python.org/3/library/tkinter.html), as well as the [Custom Tkinter library](https://github.com/TomSchimansky/CustomTkinter) to build the GUI for our project. Additionally, we used a [SQLite](https://www.sqlite.org/index.html) database to store user login info and information related to their moods and activities.

 ## Final deliverable
 
 ## Screenshots
 <img src="assets/menu_dark.png" alt="Dark Menu" height="300" width="400"/>
 <img src="assets/menu_light.png" alt="Light Menu" height="300" width="400"/>
 
## Installation/Usage 
 Start off by creating a virtual environment and activating it by running the following:
 ```
 $ python3 -m venv .venv
 $ source .venv/bin/activate
 ```
 Then install the required modules by running:
 ```
 $ pip3 install -r requirements.txt
 ```
 Lastly, run the program with:
 ```
 $ python3 moodtivity.py
 ```
## How to use
 1. Register an account
 2. Login with your new account
 3. Select from the menu what you want to do. To input your mood, select the "Enter Mood" button
 4. To be recommended an activity, select the "Find Activity" button
 
