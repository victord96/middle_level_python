from account import Account

class User(Account):
    

    def __init__(self, id, name, document) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.document = document