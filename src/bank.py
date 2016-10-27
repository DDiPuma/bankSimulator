# Dominic DiPuma
# Programming Methodology 2
# Project 1 - Bank Simulation

import customer as c
import event as e
import event_record as er
import teller as t

class Bank:
    """The Bank class is firstly a container for the queue, tellers, time,
    and events. It also contains the basic logic of what a turn entails."""

    def __init__(self, service_time = 1):
        self._time = 0

        self._customer_queue = []
        self._event_record = er.EventRecord()
        self._tellers = []

    def hire_tellers(self, n):
        for i in range(0,n):
            self._hire_teller()

    def _hire_teller(self):
        new_teller = t.Teller()
        self._tellers.append(t)

    def simulate_tick(self):
        # Increment the time
        self._time += 1

        # Check for free tellers, and give them customers
        for teller in self._tellers:
            if ~teller.has_customer() and self._are_customers_in_queue():
                teller.take_customer(self._customer_queue.pop(0))

        # Make all the tellers work
        for teller in self._tellers:
            teller.work_one_turn()
    
    def save_event(self, event):
        pass

    def get_time(self):
        return self._time

    def num_of_tellers(self):
        return len(self._tellers)

    def length_of_queue(self):
        return len(self._customer_queue)

    def _are_customers_in_bank(self):
        if _are_customers_in_queue():
            return 1
        for teller in self._tellers:
            if teller.has_customer():
                return 1

        return 0

    def are_customers_in_queue(self):
        return self.num_of_customers() > 0

    def customers_arrive(self, num_customers, service_time = 1):
        for i in range(0, num_customers):
            self._customer_queue.append(c.Customer(self, service_time))
