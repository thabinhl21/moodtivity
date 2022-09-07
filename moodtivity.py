import tkinter as tk
from data import Data
from user import *
import sqlite3 as db
from tkinter import messagebox
import customtkinter
from main import *

import matplotlib

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg,
     NavigationToolbar2Tk
 )          


class GuiApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        self.geometry("640x740")
        self.title("Moodtivity")
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LoginWindow, RegisterWindow, MenuWindow, MoodWindow, ActivityWindow,
                   EditActivities,EditMoods,ViewGoals, MoodCount,
                   ActivityCount,MoodChart,GoalsWindow
                   #EntriesWindow
                   #ActivityHistory,
                  #MoodHistory
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(LoginWindow)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)

        username = tk.StringVar()
        password = tk.StringVar()

        # if login is valid, user will be directed to the menu page
        def login():
            data = Data("authData")
            conn = db.connect("moodtivity.db")
            cur = conn.cursor()
            # checks to see if the table authData exists
            listOfTables = cur.execute(
            """SELECT name FROM sqlite_master WHERE type='table'
            AND name='authData' """).fetchall()
            # if the table authData exists, then proceed with login validation
            if listOfTables != []:
                cur.execute("SELECT * FROM authData WHERE username = ?", (username.get(),))
                row = cur.fetchone()    # gets the username and password from database
            
                # if neither the username or password exists in the database, user will be told to register
                if not row:
                    messagebox.showinfo("info", "Please register to login.")
                
                # else if the username exists, but the password is wrong, user will be told to try again
                else:
                    if listOfTables != []:
                        found = True
                    else:
                        found = False

                    if not found:
                        messagebox.showinfo("info", "Please register to login.")
                    else:
                        hashed = data.get_user_login(username.get(), password.get())[1]  # gets the hashed password from the database
                        new_bytes = password.get().encode("utf-8")
                        result = bcrypt.checkpw(new_bytes, hashed)  # compares the password the user input to the one in the database
                        if result:
                            global u_name
                            u_name = username.get()
                            showMenu = controller.show_frame(MenuWindow)
                            return showMenu
                        else:
                            messagebox.showinfo("info", "Login Invalid. Please try again.")
            # if the table authData does not exist, user will be told to register before logging in
            else:
                messagebox.showinfo("info", "Please register to login.")
            conn.commit()
            conn.close()

        login_label = customtkinter.CTkLabel(master=self, text="Login", fg_color=("#ffffff", "#1a1a1a"), text_font=("Arial", 45))
        username_label = customtkinter.CTkLabel(master=self, text="Username", fg_color=("#ffffff", "#1a1a1a"), text_font=("Arial", 20))
        username_entry = customtkinter.CTkEntry(master=self, width=250, height=25, corner_radius=10, text_font=("Arial", 18), fg_color=("#ffffff"), text_color=("#1a1a1a"), textvariable=username)
        password_entry = customtkinter.CTkEntry(master=self, show="*", width=250, height=25, corner_radius=10, text_font=("Arial", 18), fg_color=("#ffffff"), text_color=("#1a1a1a"), textvariable=password)
        password_label = customtkinter.CTkLabel(master=self, text="Password", fg_color=("#ffffff", "#1a1a1a"), text_font=("Arial", 20))
        login_button = customtkinter.CTkButton(master=self, width=120, height=32, border_width=0, corner_radius=8, text="Login",  text_font=("Arial", 18), command=lambda: login())
        register_button = customtkinter.CTkButton(master=self, width=120, height=32, border_width=0, corner_radius=8, text="Register", text_font=("Arial", 17), command=lambda: controller.show_frame(RegisterWindow))

        login_label.grid(row=0, column=1, columnspan=2, sticky="nsew", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=15)
        password_label.grid(row=2,column=0)
        password_entry.grid(row=2,column=1, pady=15)
        login_button.grid(row=3, column=1, columnspan=2, pady=10)
        register_button.grid(row=4, column=1, columnspan=2, pady=10)



class RegisterWindow(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)

        username = tk.StringVar()
        password = tk.StringVar()

        # when user hits the register button, a new table will be created in the database containing username and password info
        # password will be hashed
        # the new username and hashed password will also be inserted into the data table
        def register():
            newUser = User(username.get(), password.get())
            data = Data("authData")
            data.create_user_table()
            data.insert_login_data(newUser.get_username(), newUser.get_password())
            backToLogin = controller.show_frame(LoginWindow)
            return backToLogin

        register_label = customtkinter.CTkLabel(master=self, text="Register", fg_color=("#ffffff", "#1a1a1a"), text_font=("Arial", 45))
        username_label = customtkinter.CTkLabel(master=self, text="Username", fg_color=("#ffffff", "#1a1a1a"), text_font=("Arial", 20))
        username_entry = customtkinter.CTkEntry(master=self, width=250, height=25, corner_radius=10, text_font=("Arial", 18), fg_color=("#ffffff"), text_color=("#1a1a1a"), textvariable=username)
        password_entry = customtkinter.CTkEntry(master=self, show="*", width=250, height=25, corner_radius=10, text_font=("Arial", 18), fg_color=("#ffffff"), text_color=("#1a1a1a"), textvariable=password)
        password_label = customtkinter.CTkLabel(master=self, text="Password", fg_color=("#ffffff", "#1a1a1a"), text_font=("Arial", 20))
        register_button = customtkinter.CTkButton(master=self, width=120, height=32, border_width=0, corner_radius=8, text="Register", text_font=("Arial", 17), command=lambda: register())
        back_button = customtkinter.CTkButton(master=self, width=120, height=32, border_width=0, corner_radius=8, text="Back",  text_font=("Arial", 18), command= lambda: controller.show_frame(LoginWindow))


        register_label.grid(row=0, column=1, columnspan=2, sticky="nsew", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=15)
        password_label.grid(row=2,column=0)
        password_entry.grid(row=2,column=1, pady=15)
        register_button.grid(row=3, column=1, columnspan=2, pady=10)
        back_button.grid(row=4, column=1, columnspan=2, pady=10)

class MenuWindow(tk.Frame):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)

        # self.title("CustomTkinter complex_example.py")
        # self.geometry(f"{MenuWindow.WIDTH}x{MenuWindow.HEIGHT}")
        # self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create three frames ============

        # configure grid layout (3x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=200,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe",padx=20, pady=20)

        self.frame_center = customtkinter.CTkFrame(master=self,
                                                 width=400,
                                                 corner_radius=0)
        self.frame_center.grid(row=0, column=1, sticky="nswe",padx=10, pady=20)
        
        self.frame_right = customtkinter.CTkFrame(master=self,width=180,
                                                 corner_radius=0)
        self.frame_right.grid(row=0, column=2, sticky="nswe", padx=20, pady=20)

        # ============ frame_center ============

        # configure grid layout (1x11)
        self.frame_center.grid_rowconfigure(0, minsize = 20)   # empty row with minsize as spacing
        self.frame_center.grid_rowconfigure(9, weight = 0)  # empty row as spacing
        self.frame_center.grid_rowconfigure(13, minsize=10)    # empty row with minsize as spacing
        self.frame_center.grid_rowconfigure(20, minsize=10)  # empty row with minsize as spacing
        self.frame_center.columnconfigure(0, weight=1)
        self.frame_center.columnconfigure(1, weight=0)
        self.label_1 = customtkinter.CTkLabel(master=self.frame_center,
                                              text="Today's Mood",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10,sticky="nsew")

        self.button_1 = customtkinter.CTkButton(master=self.frame_center,
                                                text="Enter Mood",
                                                command=lambda: controller.show_frame(MoodWindow))
        self.button_1.grid(row=1, column=0, pady=10, padx=20,sticky="nsew")        

        self.label_2 = customtkinter.CTkLabel(master=self.frame_center,
                                              text="Activty Recomender",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=3, column=0, pady=10, padx=10,sticky="nsew")


        self.button_2 = customtkinter.CTkButton(master=self.frame_center,
                                                      text="Find Activity",
                                                     command=lambda: controller.show_frame(ActivityWindow))
        self.button_2.grid(row=4, column=0, pady=10, padx=20,sticky="nsew")
        
        self.label_3 = customtkinter.CTkLabel(master=self.frame_center,
                                                   text="Activity of the Day:  Yoga",
                                                   height=100,
                                                   fg_color=("white", "gray38")  # <- custom tuple-color
                                                   )
        self.label_3.grid(column=0, row=5, padx=10, pady=10,sticky="nsew")

        self.label_4 = customtkinter.CTkLabel(master=self.frame_center,
                                              text="Goals",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_4.grid(row=6, column=0, pady=10, padx=10,sticky="nsew")

        self.button_3 = customtkinter.CTkButton(master=self.frame_center,
                                                text="Enter Goal",
                                                command=lambda: controller.show_frame(GoalsWindow))
        self.button_3.grid(row=7, column=0, pady=10, padx=20,sticky="nsew")

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=20, column=0, pady=10, padx=20,sticky="nsew")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_center,
                                                        values=["Light", "Dark", "System"],
                                                        command = self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20)
        

       # ============ frame_left ============

        # configure grid layout (3x7)
        self.frame_left.rowconfigure(0, weight=0)
        #self.frame_right.rowconfigure(0, weight=1)
        #self.frame_info.grid_rowconfigure(11, minsize=10)
        self.frame_left.columnconfigure(0, weight=1)
        self.frame_left.columnconfigure(1, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_left)
        self.frame_info.grid(row=1, column=0, columnspan=1, rowspan=1,pady=20, padx=20, sticky="nsew")
        
        self.frame_info2 = customtkinter.CTkFrame(master=self.frame_left)
        self.frame_info2.grid(row=2, column=0, columnspan=1, rowspan=1, pady=20, padx=20, sticky="nsew")

        self.frame_info3 = customtkinter.CTkFrame(master=self.frame_left)
        self.frame_info3.grid(row=3, column=0, columnspan=1, rowspan=1, pady=20, padx=20, sticky="nsew")

         # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        self.frame_info.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_info.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_info.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_5 = customtkinter.CTkLabel(master=self.frame_info,
                                              text="Mood Chart",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_5.grid(row=1, column=0,sticky ="nwe", pady=0, padx=0)

    

        self.button_4 = customtkinter.CTkButton(master=self.frame_info,
                                                      text="View",
                                                     command=lambda: controller.show_frame(MoodChart))
        self.button_4.grid(row=3, column=0, pady=15, padx=15)


        # ============ frame_info2 ============

        # configure grid layout (1x1)
        self.frame_info2.rowconfigure(0, weight=1)
        self.frame_info2.columnconfigure(0, weight=1)
        self.frame_info2.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_info2.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_info2.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        
        self.label_6 = customtkinter.CTkLabel(master=self.frame_info2,
                                              text="Mood Count",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_6.grid(row=0, column=0,sticky ="nwe", pady=10, padx=10)

        self.button_5 = customtkinter.CTkButton(master=self.frame_info2,
                                                      text="View",
                                                     command=lambda: controller.show_frame(MoodCount))
        self.button_5.grid(row=1, column=0, pady=15, padx=15)

        


       
            # ============ frame_info3 ============

        # configure grid layout (1x1)
        self.frame_info3.rowconfigure(0, weight=1)
        self.frame_info3.columnconfigure(0, weight=1)
        self.frame_info3.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_info3.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_info3.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        
        self.label_7 = customtkinter.CTkLabel(master=self.frame_info3,
                                              text="Activity Count",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_7.grid(row=1, column=0,sticky ="nwe", pady=10, padx=10)

        self.button_5 = customtkinter.CTkButton(master=self.frame_info3,
                                                      text="View",
                                                     command=lambda: controller.show_frame(ActivityCount))
        self.button_5.grid(row=2, column=0, pady=15, padx=15)
        
       


            #===================Label========================
        self.label_8 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Performance",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_8.grid(row=0, column=0, pady=10, padx=10)
        #self.label_2 = customtkinter.CTkLabel(master=self.frame_center,
                                              #text="Average Daily Mood",
                                              #text_font=("Roboto Medium", -16))  # font name and size in px
        #self.label_2.grid(row=4, column=0, pady=10, padx=10)

         
        # ============ frame_right ============

        
        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Sign out"])
        self.combobox_1.grid(row=0, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.button_4 = customtkinter.CTkButton(master=self.frame_right,
                                                text="View Mood History",
                                                command=lambda: controller.show_frame(MoodHistory))
        self.button_4.grid(row=1, column=2, pady=10, padx=20,sticky ="nwe")
        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="View Activity History",
                                                command=lambda: controller.show_frame(ActivityHistory))
        self.button_5.grid(row=2, column=2, pady=10, padx=20,sticky ="nwe")

        self.button_6 = customtkinter.CTkButton(master=self.frame_right,
                                                text="View Entries",
                                                command=lambda: controller.show_frame(EntriesWindow))
        self.button_6.grid(row=3, column=2, pady=10, padx=20,sticky ="nwe")
        
        self.button_7 = customtkinter.CTkButton(master=self.frame_right,
                                                text="View Goals",
                                                command=lambda: controller.show_frame(ViewGoals))
        self.button_7.grid(row=4, column=2, pady=10, padx=20,sticky ="nwe")
        
        self.button_8 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Edit Moods",
                                            command=lambda: controller.show_frame(EditMoods))
        self.button_8.grid(row=5, column=2, pady=10, padx=20,sticky ="nwe")
        
        self.button_9 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Edit Activities",
                                                command=lambda: controller.show_frame(EditActivities))
        self.button_9.grid(row=6, column=2, pady=10, padx=20,sticky ="nwe")

       
       # set default values
        self.optionmenu_1.set("Dark")
        self.combobox_1.set("Home")
        # self.radio_button_1.select()

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

class MoodWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)

        # root = mood.CTk()
        # root.title("Mood")
        selected = tk.StringVar()
        # v.set(1)  # initializing the choice, i.e. Python

        moods = ["Terrible",
                "Bad", "Meh",
                "Good","Great"]


        def ShowChoice():
            print(selected.get())

        date = tk.StringVar()
        customtkinter.CTkLabel(master=self, text="Enter today's date:", fg_color=("gray70", "gray25"), justify = customtkinter.LEFT, padx = 30).pack()
        customtkinter.CTkEntry(master=self, width=250, height=25, corner_radius=10, text_font=("Arial", 18), fg_color=("#ffffff"), text_color=("#1a1a1a"), textvariable=date).pack()

        customtkinter.CTkLabel(self, 
                text="""Choose your current Mood:""", fg_color=("gray70", "gray25"),
                justify = customtkinter.LEFT, 
                padx = 20).pack()

        for moody in moods:
            #for i in val:
            customtkinter.CTkRadioButton(self, 
                            text = moody, 
                            padx = 20, 
                            variable = selected, value = moody,
                            command = lambda: ShowChoice()
                        ).pack(anchor=customtkinter.W)

        # Submit Button
        ## insert date and mood into database upon selecting the submit button
        def insert_mood_date():
            data = Data("moodData")
            data.create_mood_table()
            data.insert_mood(u_name, date.get(), selected.get())
            return controller.show_frame(MenuWindow)
    
        B = customtkinter.CTkButton(master = self, text ="Submit", command=lambda: insert_mood_date())
        B.pack()

        # Back button
        customtkinter.CTkButton(master=self, text="Back", pady = 1, command= lambda: controller.show_frame(MenuWindow)).pack()

class ActivityWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)

        date = tk.StringVar()
        customtkinter.CTkLabel(master=self, text="Enter today's date:", fg_color=("gray70", "gray25"), justify = customtkinter.LEFT, padx = 30).pack()
        customtkinter.CTkEntry(master=self, width=250, height=25, corner_radius=10, text_font=("Arial", 18), fg_color=("#ffffff"), text_color=("#1a1a1a"), textvariable=date).pack()

        # suggest activities then store username, date, and activity in new table
        def find_activities():
            act = FindActivity()
            x = act.rec_activity()
            active = Data("activityTable")
            active.create_activity_table()
            active.insert_activity(u_name, date.get(), x)
            return controller.show_frame(MenuWindow)

        customtkinter.CTkButton(self, 
                text="""Find Activity:""",
                padx = 20, command= lambda: find_activities()).pack()

        

        B = customtkinter.CTkButton(master = self, text ="Back", pady = 1,
                                    command=lambda: controller.show_frame(MenuWindow))
        B.pack()    


class GoalsWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)


        customtkinter.CTkLabel(self, 
                text="""Enter your Goals:""", fg_color=("gray70", "gray25"),
                justify = customtkinter.LEFT, 
                padx = 20).pack()


        #Submit Button
        def button_function():
            print("button pressed")
        B = customtkinter.CTkButton(master = self, text ="Back",
                                    command=lambda: controller.show_frame(MenuWindow))
        B.pack()


class MoodHistory(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)


        customtkinter.CTkLabel(self, 
                text="""Mood History:""", fg_color=("gray70", "gray25"),
                justify = customtkinter.LEFT, 
                padx = 20).pack()
        
        # take the data
        lst = [('Date','Mood'),('07/22','Meh'),('07/23','Good'),('07/24','Meh'),
	             ('07/25','Meh')]
        total_rows = len(lst)
        total_columns = len(lst[0])
        
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = customtkinter.CTkEntry(width=100, fg='blue')
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, lst[i][j])


        #Submit Button
        def button_function():
            print("button pressed")
        B = customtkinter.CTkButton(master = self, text ="Back",
                                    command=lambda: controller.show_frame(MenuWindow))
        B.pack()
        
  
class ActivityHistory(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)
        customtkinter.CTkLabel(self, 
                text="""Activity History:""", fg_color=("gray70", "gray25"),
                justify = customtkinter.LEFT, 
                padx = 20).pack()
        
        lst = [('Date','Activity'),('07/22','Walk'),('07/23','Game'),('07/24','Faith'),
                 ('07/25','Walk')]
        total_rows = len(lst)
        total_columns = len(lst[0])
        
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = customtkinter.CTkEntry(width=100, fg='blue')
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, lst[i][j])
                
        
        B = customtkinter.CTkButton(master = self, text ="Submit", 
                                  command=lambda: controller.show_frame(MenuWindow))
        B.pack()

        
class EntriesWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)

        matplotlib.use('TkAgg')
        customtkinter.CTkLabel(master = self, 
                text="""Entries Entered:""", fg_color=("gray70", "gray25"), 
                padx = 20).pack()
        
        # take the data
        lst = [('Date','Entries'),('07/22','Blah.....'),('07/23','Blah...Blah'),
	      ('07/24','Blah...Blah'),
	      ('07/25','Blah...Blah')]

# find total number of rows and
# columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = customtkinter.CTkEntry(width=100, fg='blue')
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, lst[i][j])


        #Submit Button
        def button_function():
            print("button pressed")
        B = customtkinter.CTkButton(master = self, text ="Back",
                                    command=lambda: controller.show_frame(MenuWindow))
        B.pack()

class ViewGoals(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)


        customtkinter.CTkLabel(self, 
                text="""All Goals:""", fg_color=("gray70", "gray25"),
                justify = customtkinter.LEFT, 
                padx = 20).pack()


        #Submit Button
        def button_function():
            print("button pressed")
        B = customtkinter.CTkButton(master = self, text ="Back",
                                    command=lambda: controller.show_frame(MenuWindow))
        B.pack()
        

class EditMoods(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)


        customtkinter.CTkLabel(self, 
                text="""Edit Moods:""", fg_color=("gray70", "gray25"),
                justify = customtkinter.LEFT, 
                padx = 20).pack()


        #Submit Button
        def button_function():
            print("button pressed")
        B = customtkinter.CTkButton(master = self, text ="Back",
                                    command=lambda: controller.show_frame(MenuWindow))
        B.pack()

        
class EditActivities(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)


        customtkinter.CTkLabel(self, 
                text="""Edit Activites:""", fg_color=("gray70", "gray25"),
                justify = customtkinter.LEFT, 
                padx = 20).pack()


        #Submit Button
        def button_function():
            print("button pressed")
        B = customtkinter.CTkButton(master = self, text ="Back",
                                    command=lambda: controller.show_frame(MenuWindow))
        B.pack()

class MoodCount(tk.Frame):
     def __init__(self, parent, controller):
        

         tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)
         matplotlib.use('TkAgg')

         

         # prepare data
         data = {
             'Terrible': 3,
             'Bad': 7,
             'Meh':6 ,
             'Good': 7,
             'Great': 5
         }
         moods = data.keys()
         count = data.values()

         # create a figure
         figure = Figure(figsize=(6, 4), dpi=100)

         # create FigureCanvasTkAgg object
         figure_canvas = FigureCanvasTkAgg(figure, self)

         # create the toolbar
         NavigationToolbar2Tk(figure_canvas, self)

         # create axes
         axes = figure.add_subplot()

         # create the barchart
         axes.bar(moods, count)
         axes.set_ylabel('Count')

         figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
         B = customtkinter.CTkButton(master = self, text ="Return",
                                     command=lambda: controller.show_frame(MenuWindow))
         B.pack()
class MoodChart(tk.Frame):
     def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)
         matplotlib.use('TkAgg')
         

         # prepare data
         data = {
             'Terrible': 21,
             'Bad': 22,
             'Meh': 21,
             'Good': 24,
             'Great': 25
         }
         moods = data.keys()
         dates = data.values()

         # create a figure
         figure = Figure(figsize=(4, 4), dpi=100)

         # create FigureCanvasTkAgg object
         figure_canvas = FigureCanvasTkAgg(figure, self)

         # create the toolbar
         NavigationToolbar2Tk(figure_canvas, self)

         # create axes
         axes = figure.add_subplot()

         # create the barchart
         axes.plot(dates, moods)
         axes.set_ylabel('Mood')
         axes.set_xlabel('Dates')
         axes.margins(0)
         figure.tight_layout()
         axes.axis('tight')

         figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
         B = customtkinter.CTkButton(master = self, text ="Return",
                                     command=lambda: controller.show_frame(MenuWindow))
         B.pack()

class ActivityCount(tk.Frame):
     def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent, bg="#1a1a1a", pady=50, padx=50)
         matplotlib.use('TkAgg')

         # prepare data
         data = {
             'Sleep': 3,
             'Faith': 7,
             'Vent':6 ,
             'Pet': 7,
             'Drive': 5,
             'Nature': 0,
             'Comedy': 7,
             'Game': 10,
             'Read': 0,
             'Breathe': 7,
             'Self-care': 7,
             'Socialize': 7,
             'Exercise': 7,
             'Write': 7,
             'Errands': 7,
             'Yoga': 7,
             'Meditate': 7,
             'Music': 7,
             'Bathe': 7,
             'Create': 7



         }
         languages = data.keys()
         popularity = data.values()

         # create a figure
         figure = Figure(figsize=(6, 4), dpi=100)

         # create FigureCanvasTkAgg object
         figure_canvas = FigureCanvasTkAgg(figure, self)

         # create the toolbar
         NavigationToolbar2Tk(figure_canvas, self)

         # create axes
         axes = figure.add_subplot()

         # create the barchart
         axes.bar(languages, popularity)
         axes.set_ylabel('Count')

         figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

         B = customtkinter.CTkButton(master = self, text ="Return",
                                     command=lambda: controller.show_frame(MenuWindow))
         B.pack()


app = GuiApp()
app.mainloop()



