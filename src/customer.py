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
        self._time_departed = None
        self._time_at_teller = 0

        self._bank = None
        self._teller = None

    def accept_teller_service(self):
        self._time_at_teller += 1

        if self._time_at_teller >= self._service_time:
            self.leave_bank()
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
        return self._arrival_time

    def get_time_reached_teller(self):
        return self._time_reached_teller

    def get_time_departed(self):
        return self.time_departed

    def get_wait_time(self):
        return self._time_reached_teller - self._arrival_time

    def get_total_time(self):
        return self._time_departed - self._arrival_time
