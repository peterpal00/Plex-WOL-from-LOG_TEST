from datetime import datetime

class User:
    def __init__(self, Address, ID, Name,) -> None:
        self.address = Address
        self.id = ID
        self.name = Name
        self.login_time = datetime.now()




