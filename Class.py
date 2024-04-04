class User:
    def _init_(self, username, name, email):
        self.username =  username
        self.name = name
        self.email = email
        print("User Created!")
    user1 =User("Diyo", "Peter Diyo", "princediyo93@gmail.com")  
    print(user1)  