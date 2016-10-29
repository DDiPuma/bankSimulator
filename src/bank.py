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
    _current_id = 0

    def __init__(self, service_time = 1):
        self._id = self.__class__._current_id
        self.__class__._current_id += 1

        self._time = 1

        self._customer_queue = []
        self._event_record = er.EventRecord()
        self._tellers = []

    def hire_tellers(self, n):
        # Add a number of tellers to the bank
        for i in range(0,n):
            new_teller = t.Teller()
            self._tellers.append(new_teller)

    def customers_arrive(self, num_customers, service_time = 1):
        # Add a number of customers with a given service time to the queue
        for i in range(0, num_customers):
            self._customer_queue.append(c.Customer(self, service_time))

    def simulate_tick(self):
        # Check for free tellers, and give them customers, if there are any
        # This is advancing the queue, fundamentally
        for tell in self._tellers:
            if ~tell.has_customer() and self.are_customers_in_queue():
                # List.pop(0) is the Pythonic method of queueing without
                # using importing a queue library
                tell.take_customer(self._customer_queue.pop(0))

        # Make all the tellers work
        for tell in self._tellers:
            tell.work_one_turn()
    
        # Increment the time
        self._time += 1

    def save_event(self, event):
        self._event_record.add_event(event)

    # The below methods are dumb-ish getters
    def get_time(self):
        return self._time

    def num_of_tellers(self):
        return len(self._tellers)

    def length_of_queue(self):
        return len(self._customer_queue)

    def _are_customers_in_bank(self):
        if _are_customers_in_queue():
            return True
        for tell in self._tellers:
            if tell.has_customer():
                return True

        return False

    def are_customers_in_queue(self):
        return self.length_of_queue() > 0

    def get_id(self):
        return self._id
