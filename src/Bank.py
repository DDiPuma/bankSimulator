# Dominic DiPuma
# Programming Methodology 2
# Project 1 - Bank Simulation

# DO A LOT OF IMPORTS

class Bank:
    """The Bank class contains all of the simulated people, the events, and
    is responsible for the execution of simulation logic"""

    def __init__(self, num_tellers, arrival_rate, service_time = 1):
        self._arrival_rate = arrival_rate
        self._service_time = service_time

        self._customer_queue = []
        self._event_record = []
        self._tellers = []

        for i in range(0, num_tellers):
            add_teller()

    def customer_arrives(self):
        self._customer_queue.append(

    def hire_teller(self):
        

    def simulate_tick(self):

    
    def store_event(self, event):

