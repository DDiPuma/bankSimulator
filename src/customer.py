# Dominic DiPuma

"""Contains the Customer class"""

import event as e

class Customer:
    current_id = 0

    def __init__(self, bank, service_time = 1):
        """Constructing the customer should send the bank an Event"""
        # Most of these assignments are null
        self._id = self.__class__.current_id
        self.__class__.current_id += 1

        self._service_time = service_time

        self._bank = bank
        self._arrival_time = self._time()

        self._time_reached_teller = None
        self._departure_time = None
        self._time_at_teller = 0

        self._teller = None

        arrival_event = e.CustomerArrivalEvent(self, self._arrival_time)
        self._bank.save_event(arrival_event)

    def accept_teller_service(self):
        """Decide whether customer is done, and return that status to the teller"""
        if self._time_reached_teller == None:
            raise Exception('Customer is not at a teller!')

        self._time_at_teller += 1

        if self._time_at_teller >= self._service_time:
            self._departure_time = self._time() 
            self.leave_bank()
            return True

        return False

    def go_to_teller(self, teller):
        """Assign the customer to a teller, and send the bank an Event"""
        self._time_reached_teller = self._time()
        self._teller = teller

        service_event = e.CustomerServiceEvent(self, teller, 
                self._time_reached_teller)
        self._bank.save_event(service_event)

    def leave_bank(self):
        """Have the customer leave the bank, and send the bank an Event"""
        departure_event = e.CustomerDepartureEvent(self, self._departure_time)
        self._bank.save_event(departure_event)
        self._bank = None

    # Below this point there are mostly dumb getter methods
    def get_id(self):
        return self._id

    def get_bank_id(self):
        return self._bank.get_id()

    def get_arrival_time(self):
        if self._arrival_time == None:
            raise Exception('Customer is not at a bank!')

        return self._arrival_time

    def get_time_reached_teller(self):
        if self._time_reached_teller == None:
            raise Exception('Customer is not at a teller!')

        return self._time_reached_teller

    def get_departure_time(self):
        if self._departure_time == None:
            raise Exception('Customer has not departed!')

        return self._departure_time

    def get_wait_time(self):
        if self._time_reached_teller == None:
            raise Exception('Customer is not done waiting!')

        return self._time_reached_teller - self._arrival_time

    def get_total_time(self):
        if self._departure_time == None:
            raise Exception('Customer has not departed!')

        return self.get_wait_time() + self._service_time

    def _time(self):
        """Abstract away the process of getting time to prevent copypaste code.
           Also, helps in unit testing by getting rid of the bank dependency"""
        if self._bank == None:
            return 0

        return self._bank.get_time()
