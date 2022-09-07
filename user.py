import bcrypt

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username 

    def get_password(self):
        return self.hash_password()

    # converts password string to a hash to be securely stored in databased
    def hash_password(self):
        bytePass = self.password.encode("utf-8")    # converts to an array of bytes
        salt = bcrypt.gensalt() # generate salt
        hash = bcrypt.hashpw(bytePass, salt)
        return hash

