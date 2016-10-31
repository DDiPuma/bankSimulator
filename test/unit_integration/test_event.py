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

class TestCustomerServiceEvent:
    def test_id_increments(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        tell = t.Teller()
        service1 = e.CustomerServiceEvent(1, cust, tell)
        service2 = e.CustomerServiceEvent(1, cust, tell)

        assert service2.get_id() == service1.get_id() + 1

class TestCustomerDepartureEvent:
    def test_id_increments(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        departure1 = e.CustomerDepartureEvent(1, cust)
        departure2 = e.CustomerDepartureEvent(1, cust)

        assert departure2.get_id() == departure1.get_id() + 1
