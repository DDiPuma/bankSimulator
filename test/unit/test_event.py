# Dominic DiPuma

import sys
sys.path.append("src/")
import event as e
import bank as b
import customer as c
import teller as t

class TestEvent:
    def test_id_increments(self):
        first_event = e.Event(1)
        second_event = e.Event(1)

        assert second_event.get_id() == first_event.get_id() + 1


class TestCustomerArrivalEvent:
    def test_id_increments(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        arrival1 = e.CustomerArrivalEvent(1, cust)
        arrival2 = e.CustomerArrivalEvent(1, cust)

        assert arrival2.get_id() == arrival1.get_id() + 1

    def test_output_is_sane(self):
        sample_bank = b.Bank()
        sample_bank.simulate_tick()

        cust = c.Customer(sample_bank)

        arrival = e.CustomerArrivalEvent(sample_bank.get_time(), cust)

        # FIGURE OUT HOW TO PROPERLY TEST OUTPUT
        assert 1

class TestCustomerServiceEvent:
    pass
