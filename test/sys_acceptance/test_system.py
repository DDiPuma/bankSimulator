# Dominic DiPuma

import sys
sys.path.append("src/")
import bank as b
import event as e

class TestSystem:
    def test_ten_turns_one_teller(self):
        bank = b.Bank()
        bank.hire_tellers(1)

        for i in range(10):
            bank.customers_arrive(10, 1)
            bank.simulate_tick()

        while bank.are_customers_in_bank():
            bank.simulate_tick()

        events = bank.get_event_record()

        # Ensure 300 events are in system
        # There are 100 customers, each of whom generates 3 events
        assert len(events.get_event_list()) == 300

        # And ensure that the last event occurs in the 100th tick
        assert events.get_event_list()[-1].get_time() == 100

    def test_ten_turns_ten_tellers(self):
        bank = b.Bank()
        bank.hire_tellers(10)

        for i in range(10):
            bank.customers_arrive(10, 1)
            bank.simulate_tick()

        while bank.are_customers_in_bank():
            bank.simulate_tick()

        events = bank.get_event_record()

        # Ensure 300 events are in system
        # There are 100 customers, each of whom generates 3 events
        assert len(events.get_event_list()) == 300

        # And ensure that the last event occurs in the 10th tick
        assert events.get_event_list()[-1].get_time() == 10

        # And also check that every customer waits 0 turns
        departures = events.filter_by_type(
            e.CustomerDepartureEvent).get_event_list()
        
        wait_times = [event.get_wait_time() for event in departures]
        assert wait_times.count(0) == 100

        # And check that every one of them is in the bank for 1 turn
        total_times = [event.get_total_time() for event in departures]
        assert total_times.count(1) == 100
