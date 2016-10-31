# Dominic DiPuma
# Programming Methodology 2
# Project 1 - Bank Simulation

"""Contains the Bank class"""

import customer as c
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

    def hire_tellers(self, num_tellers):
        """Add a number of tellers to the bank"""
        for i in range(0,num_tellers):
            new_teller = t.Teller()
            self._tellers.append(new_teller)

    def customers_arrive(self, num_customers, service_time = 1):
        """Add a number of customers with service time (optional) to the queue"""
        for i in range(0, num_customers):
            self._customer_queue.append(c.Customer(self, service_time))

    def simulate_tick(self):
        """Simulate a single tick of the bank

        The process of a tick is to advance the queue, then have the tellers work,
        and finally to increment the time attribute"""
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

    # Methods to follow are fairly straightfoward
    def save_event(self, event):
        self._event_record.add_event(event)

    def get_time(self):
        return self._time

    def num_of_tellers(self):
        return len(self._tellers)

    def length_of_queue(self):
        return len(self._customer_queue)

    def are_customers_in_bank(self):
        # A customer in the bank is either in the queue or at a teller
        if self.are_customers_in_queue():
            return True
        for tell in self._tellers:
            if tell.has_customer():
                return True

        return False

    def are_customers_in_queue(self):
        return self.length_of_queue() > 0

    def get_id(self):
        return self._id

    def get_event_record(self):
        return self._event_record
