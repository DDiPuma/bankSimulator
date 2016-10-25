# Dominic DiPuma

class Event:
    current_id = 0

    def __init__(self):
        self._id = self.__class__.current_id
        self.__class__.current_id += 1
