from datetime import datetime

class User:
    def __init__(self, Address, ID, Name,) -> None:
        self.address = Address
        self.id = ID
        self.name = Name
        self.login_time = datetime.now()

    def __eq__(self, other):
        if self.address == other.address and self.id == other.id:
            return True
        else:
            False




