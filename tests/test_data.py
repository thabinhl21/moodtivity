from data import *
import unittest

class TestData(unittest.TestCase):

    def test_create_table1(self):

        table = Data("student")

        table.create_user_table()
        
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()

        listOfTables = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table'
        AND name='student' """).fetchall()
        conn.commit()
        conn.close()
        
        if listOfTables != []:
            found = True
        else:
            found = False

        self.assertEqual(found, True)
    
    def test_create_table2(self):

        table = Data("universities")

        table.create_user_table()
        
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()

        listOfTables = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table'
        AND name='universities' """).fetchall()
        conn.commit()
        conn.close()
        
        if listOfTables != []:
            found = True
        else:
            found = False

        self.assertEqual(found, True)

    def test_insert_login1(self):
        table = Data("student")

        table.insert_login_data("class", "cs100")

        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE username = ?", ("class",))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            found = True
        else:
            found = False

        self.assertEqual(found, True)

    def test_insert_login2(self):
        table = Data("universities")

        table.insert_login_data("california", "uc113948")

        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM universities WHERE username = ?", ("california",))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            found = True
        else:
            found = False

        self.assertEqual(found, True)

    def test_get_login1(self):
        table = Data("student")

        result = table.get_user_login("class", "cs100")

        self.assertEqual(result[0], "class")

    def test_get_login2(self):
        table = Data("universities")

        result = table.get_user_login("california", "uc113948")

        self.assertEqual(result[0], "california")

    def test_date_table(self):
        table = Data("days")

        table.create_date_table()
        
        conn = db.connect("moodtivity.db")
        cur = conn.cursor()

        listOfTables = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table'
        AND name='days' """).fetchall()
        conn.commit()
        conn.close()
        
        if listOfTables != []:
            found = True
        else:
            found = False

        self.assertEqual(found, True)

    def test_insert_mood(self):
        table = Data("days")

        table.insert_mood("b123", "7/19/22", "meh", "meditate")

        conn = db.connect("moodtivity.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM days WHERE username = ?", ("b123",))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            found = True
        else:
            found = False

        self.assertEqual(found, True)

    def test_get_data(self):
        table = Data("days")

        result = table.get_data("b123")

        self.assertEqual(result[0], "b123")

    
if __name__ == "__main__":
    unittest.main()