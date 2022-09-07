import sqlite3 as db

class Data:

    def __init__(self, tableName):
        self.tableName = tableName

    # create table of login data
    def create_user_table(self):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS " + self.tableName + """ (
                     username text,
                     hashPass text
                    )""")
        conn.commit()
        conn.close()

    def insert_login_data(self, username, password):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.tableName + " VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

    
    def get_user_login(self, username, password):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + self.tableName + " WHERE username = ?", (username,))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        return row

    def create_mood_table(self):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS " + self.tableName + """ (
                    username text,
                    date text,
                    mood text
                    )""")
        conn.commit()
        conn.close()

    def insert_mood(self, username, date, mood):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.tableName + " VALUES (?, ?, ?)", (username, date, mood))
        conn.commit()
        conn.close()

    def get_data(self, username):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + self.tableName + " WHERE username = ?", (username,))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        return row

    def create_activity_table(self):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS " + self.tableName + """ (
                    username text,
                    date text,
                    activity text
                    )""")
        conn.commit()
        conn.close()

    def insert_activity(self, username, date, activity):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.tableName + " VALUES (?, ?, ?)", (username, date, activity))
        conn.commit()
        conn.close()

    def get_all_rows(self, username):
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + self.tableName + " WHERE username = ?", (username,))
        row = cur.fetchall()
        conn.commit()
        conn.close()
        return row
  