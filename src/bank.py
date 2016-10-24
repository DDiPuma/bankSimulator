# Dominic DiPuma
# Programming Methodology 2
# Project 1 - Bank Simulation

from customer import Customer
from event import Event
from event_record import EventRecord
from teller import Teller

class Bank:
    """The Bank class is firstly a container for the queue, tellers, time,
    and events. It also contains the basic logic of what a turn entails."""

    def __init__(self, service_time = 1):
        self._time = 0

        self._customer_queue = []
        self._event_record = EventRecord()
        self._tellers = []

    def hire_teller(self):
        pass

    def simulate_tick(self):
        self._time += 1
    
    def store_event(self, event):
        pass

    def get_time(self):
        return self._time
