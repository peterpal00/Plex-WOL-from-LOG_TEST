from datetime import datetime

class User:
    def __init__(self, Address, Name, Login_time) -> None:
        self.address = Address
        self.name = Name
        self.login_time = datetime.now()




