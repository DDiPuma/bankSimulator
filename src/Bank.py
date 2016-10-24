# Dominic DiPuma
# Programming Methodology 2
# Project 1 - Bank Simulation

# DO A LOT OF IMPORTS

class Bank:
    """The Bank class contains all of the simulated people, the events, and
    is responsible for the execution of simulation logic"""

    def __init__(self, service_time = 1):
        self._service_time = service_time
        self._time = 0

        self._customer_queue = []
        self._tellers = []

    def hire_teller(self):
        pass

    def simulate_tick(self):
        self._time += 1
    
    def store_event(self, event):
        pass

    def get_time(self):
        return self._time
