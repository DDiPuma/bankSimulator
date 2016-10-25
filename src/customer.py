# Dominic DiPuma

import bank
import event
import teller

class Customer:
    current_id = 0

    def __init__(self, service_time = 1):
        self._id = self.__class__.current_id
        self.__class__.current_id += 1

        self._service_time = service_time

        self._arrival_time = None
        self._time_reached_teller = None
        self._departure_time = None
        self._time_at_teller = 0

        self._bank = None
        self._teller = None

    def accept_teller_service(self):
        if self._time_reached_teller == None:
            raise Exception('Customer is not at a teller!')

        self._time_at_teller += 1

        if self._time_at_teller >= self._service_time:
            self.leave_bank(self._time_reached_teller + self._service_time)
            return True

        return False

    def go_to_bank(self, time, bank):
        self._arrival_time = time
        self._bank = bank
        # PUBLISH AN EVENT

    def go_to_teller(self, time, teller):
        self._time_reached_teller = time
        self._teller = teller
        # PUBLISH AN EVENT

    def leave_bank(self, time):
        self._departure_time = time
        # PUBLISH AN EVENT

    def get_id(self):
        return self._id

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

        return self._departure_time - self._arrival_time
