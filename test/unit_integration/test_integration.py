# Dominic DiPuma

import sys
sys.path.append("src/")
import bank as b
import event as e

class TestIntegration():
    def test_one_customer(self):
        bank = b.Bank()
        bank.hire_tellers(1)
        bank.customers_arrive(1, 1)

        bank.simulate_tick()

        event_list = bank.get_event_record().get_event_list()

        # Check that all 3 events for the one customer are recorded in order
        assert type(event_list[0]) == e.CustomerArrivalEvent
        assert type(event_list[1]) == e.CustomerServiceEvent
        assert type(event_list[2]) == e.CustomerDepartureEvent

        # Check that the date for the departure event is accurate
        assert event_list[2].get_wait_time() == 0
        assert event_list[2].get_total_time() == 1

    def test_two_customers_two_turns_of_service(self):
        bank = b.Bank()
        bank.hire_tellers(1)
        bank.customers_arrive(2, 2)

        # First customer gets 2 turns of service
        bank.simulate_tick()
        bank.simulate_tick()
        # Second gets 2 turns of service
        bank.simulate_tick()
        bank.simulate_tick()

        # Should have six events now
        # Two arrivals, a service, a departure, a service, and a departure

        event_list = bank.get_event_record().get_event_list()

        assert type(event_list[0]) == e.CustomerArrivalEvent
        assert type(event_list[1]) == e.CustomerArrivalEvent
        assert type(event_list[2]) == e.CustomerServiceEvent
        assert type(event_list[3]) == e.CustomerDepartureEvent
        assert type(event_list[4]) == e.CustomerServiceEvent
        assert type(event_list[5]) == e.CustomerDepartureEvent

        # Now check the departures
        assert event_list[3].get_wait_time() == 0
        assert event_list[3].get_total_time() == 2

        assert event_list[5].get_wait_time() == 2
        assert event_list[5].get_total_time() == 4
