# Dominic DiPuma

class Event:
    current_id = 0

    def __init__(self, time):
        self._id = self.__class__.current_id
        self.__class__.current_id += 1
        
        self._time = time

    def get_id(self):
        return self._id

    def get_time(self):
        return self._time

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
        print("Tick #{0}, Bank #{1}: Customer #{2} arrives".format(
            tick, bank_id, cust_id))

class CustomerServiceEvent(Event):
    def __init__(self, customer, teller, time):
        super().__init__(time)
        self._customer = customer
        self._teller = teller

    def print(self):
        tick = self._time
        bank_id = self._customer.get_bank_id()
        cust_id = self._customer.get_id()
        tell_id = self._teller.get_id()

        print("Tick #{0}, Bank #{1}: Customer #{2} reaches Teller #{3}".format(
            tick,bank_id, cust_id, tell_id))

class CustomerDepartureEvent(Event):
    def __init__(self, customer, time):
        super().__init__(time)
        self._customer = customer

    def print(self):
        # Get all the needed data
        tick = self._time
        bank_id = self._customer.get_bank_id()
        cust_id = self._customer.get_id()

        # Create a string to print out
        print("Tick #{0}, Bank #{1}: Customer #{2} leaves".format(tick,
            bank_id, cust_id))

    def get_wait_time(self):
        return self._customer.get_wait_time()

    def get_total_time(self):
        return self._customer.get_total_time()
