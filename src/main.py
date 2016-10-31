# Dominic DiPuma

"""A sample use of the bank simulation system"""

import matplotlib.pyplot as plt

import bank as b
import event as e 

def get_average_wait_time(bank):
    """Given a bank, return the bank's average wait time
    
    This module will only read from Departure events, which means that if the
    bank is not yet empty, it will give incomplete data"""
    rec = bank.get_event_record()
    departures = rec.filter_by_type(e.CustomerDepartureEvent).get_event_list()
    wait_times = [event.get_wait_time() for event in departures]

    return sum(wait_times)/len(wait_times)

def main():
    """Simulates banks and then produces a graph of wait times"""
    NUM_OF_BANKS = 10

    # Create 10 banks in a list
    banks = [b.Bank() for i in range(NUM_OF_BANKS)]

    # Now hire tellers
    # For each number 1 to 10, get a bank and hire that many tellers
    for i in range(NUM_OF_BANKS):
        banks[i].hire_tellers(i+1)

    # The next step is to send 10 customers to each bank per turn
    # while simulating, for 10 turns
    # Each customer has a service time of 1
    for i in range(10):
        for bank in banks:
            bank.customers_arrive(10, 1)
            bank.simulate_tick()

    # Simulate ticks for each bank until the bank runs out of customers
    for bank in banks:
        while bank.are_customers_in_bank():
            bank.simulate_tick()

    average_wait_times = [get_average_wait_time(bank) for bank in banks]

    print(average_wait_times)

    plt.plot(range(1,11), average_wait_times, 'ro')
    plt.title("Dependence of customer wait time on the number of tellers at a bank")
    plt.xlabel("Number of tellers")
    plt.ylabel("Average wait time")
    plt.axis([0, 11, 0, 50])
    plt.show()

# Allows automatic execution when 'python main.py' is run
if __name__ == "__main__":
    main()
