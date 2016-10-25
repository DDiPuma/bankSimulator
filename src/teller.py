# Dominic DiPuma

class Teller:
    current_id = 0

    def __init__(self):
        _id = self.__class__.current_id
        self.__class__.current_id += 1

