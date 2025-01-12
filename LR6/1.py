class UserAccount:
    username = ""
    email = ""
    __password = ""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password

ua = UserAccount("sadov", "sad@", "1234")

print(ua.check_password("1234"))
print(ua.check_password("124"))

ua.set_password("124")

print(ua.check_password("1234"))
print(ua.check_password("124"))