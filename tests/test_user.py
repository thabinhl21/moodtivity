from user import *
import unittest

class TestUser(unittest.TestCase):

    def test_username(self):
        user1 = User("class", "cs100")
        user2 = User("bob123", "mypass")
        user3 = User("3847924", "10834597934")

        result1 = user1.get_username()
        result2 = user2.get_username()
        result3 = user3.get_username()

        self.assertEqual(result1, "class")
        self.assertEqual(result2, "bob123")
        self.assertEqual(result3, "3847924")

    def test_password_short(self):
        user1 = User("class", "cs100")
        user2 = User("bob123", "mypass")
        user3 = User("3847924", "1083934")

        pass1 = "cs100"
        pass2 = "mypass"
        pass3 = "1083934"

        byte1 = pass1.encode("utf-8")
        byte2 = pass2.encode("utf-8")
        byte3 = pass3.encode("utf-8")

        result1 = user1.get_password()
        result2 = user2.get_password()
        result3 = user3.get_password()

        hash1 = bcrypt.checkpw(byte1, result1)
        hash2 = bcrypt.checkpw(byte2, result2)
        hash3 = bcrypt.checkpw(byte3, result3)

        self.assertEqual(hash1, True)
        self.assertEqual(hash2, True)
        self.assertEqual(hash3, True)

    def test_password_long(self):
        user1 = User("username2480", "thisismypassword8204fh13994ff23")
        user2 = User("bob123", "unicorna9298402f-1fnf~!!!!")
        user3 = User("flower394", "~}]]wwerj931?.>``23~~*&^@()#*&@fhrfqoeifnwrogn@#$$$")

        pass1 = "thisismypassword8204fh13994ff23"
        pass2 = "unicorna9298402f-1fnf~!!!!"
        pass3 = "~}]]wwerj931?.>``23~~*&^@()#*&@fhrfqoeifnwrogn@#$$$"

        byte1 = pass1.encode("utf-8")
        byte2 = pass2.encode("utf-8")
        byte3 = pass3.encode("utf-8")

        result1 = user1.get_password()
        result2 = user2.get_password()
        result3 = user3.get_password()

        hash1 = bcrypt.checkpw(byte1, result1)
        hash2 = bcrypt.checkpw(byte2, result2)
        hash3 = bcrypt.checkpw(byte3, result3)

        self.assertEqual(hash1, True)
        self.assertEqual(hash2, True)
        self.assertEqual(hash3, True)

    def test_hash_short(self):
        user1 = User("username2480", "password1383")
        user2 = User("bob123", "candy20d")
        user3 = User("flower394", "00129~++")

        pass1 = "password1383"
        pass2 = "candy20d"
        pass3 = "00129~++"

        byte1 = pass1.encode("utf-8")
        byte2 = pass2.encode("utf-8")
        byte3 = pass3.encode("utf-8")

        result1 = user1.hash_password()
        result2 = user2.hash_password()
        result3 = user3.hash_password()

        hash1 = bcrypt.checkpw(byte1, result1)
        hash2 = bcrypt.checkpw(byte2, result2)
        hash3 = bcrypt.checkpw(byte3, result3)

        self.assertEqual(hash1, True)
        self.assertEqual(hash2, True)
        self.assertEqual(hash3, True)

    def test_hash_long(self):
        user1 = User("username2480", "(())++}poptart2374997..??!!@#$#@*&#&*$?][#*($*#(@930587429")
        user2 = User("bob123", "candy20d394859yuwrmgeotignwo!&#(($./,;::?'[[]")
        user3 = User("flower394", "00129~++&2384bwpqfbaoiqerfni*&(#()!#)1247385729")

        pass1 = "(())++}poptart2374997..??!!@#$#@*&#&*$?][#*($*#(@930587429"
        pass2 = "candy20d394859yuwrmgeotignwo!&#(($./,;::?'[[]"
        pass3 = "00129~++&2384bwpqfbaoiqerfni*&(#()!#)1247385729"

        byte1 = pass1.encode("utf-8")
        byte2 = pass2.encode("utf-8")
        byte3 = pass3.encode("utf-8")

        result1 = user1.hash_password()
        result2 = user2.hash_password()
        result3 = user3.hash_password()

        hash1 = bcrypt.checkpw(byte1, result1)
        hash2 = bcrypt.checkpw(byte2, result2)
        hash3 = bcrypt.checkpw(byte3, result3)

        self.assertEqual(hash1, True)
        self.assertEqual(hash2, True)
        self.assertEqual(hash3, True)


if __name__ == "__main__":
    unittest.main()