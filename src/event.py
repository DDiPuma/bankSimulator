# Dominic DiPuma

class Event:
    current_id = 0

    def __init__(self, time):
        self._id = self.__class__.current_id
        self.__class__.current_id += 1
        
        self._time = time

class CustomerArrivalEvent(Event):
    def __init__(self, customer, time):
        super().__init__(time)
        self._customer = customer

    def print(self):
        # Get all the needed data
        tick = self._time
        bank_id = self._customer.get_bank_id()
        cust_id = self._customer.get_id()

        # Create a string to print out
        print("Tick #{0}, Bank #{1}: Customer #{2} arrives".format(tick,
            bank_id, cust_id))
