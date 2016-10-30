# Dominic DiPuma

import sys
sys.path.append("src/")
import event as e
import event_record as er
import bank as b
import customer as c

class TestEventRecord:
    def test_empty_constructor(self):
        rec = er.EventRecord()
        assert rec.get_event_list() == []

    def test_constructor_with_event_list(self):
        e1 = e.Event(1)
        e2 = e.Event(1)
        e_list = [e1, e2]

        rec = er.EventRecord(e_list)
        assert rec.get_event_list() == [e1, e2]

    def test_events_add(self):
        rec = er.EventRecord()

        e1 = e.Event(1)
        rec.add_event(e1)

        assert rec.get_event_list() == [e1]

    def test_filter_by_type_returns_all(self):
        bank = b.Bank()
        cust = c.Customer(bank)

        e1 = e.CustomerArrivalEvent(1, cust)
        e2 = e.CustomerArrivalEvent(1, cust)
        e_list = [e1, e2]

        rec = er.EventRecord(e_list)

        filtered_rec = rec.filter_by_type(e.CustomerArrivalEvent)
        assert filtered_rec.get_event_list() == e_list

    def test_filter_by_type_returns_none(self):
        bank = b.Bank()
        cust = c.Customer(bank)

        e1 = e.CustomerArrivalEvent(1, cust)
        e2 = e.CustomerArrivalEvent(1, cust)
        e_list = [e1, e2]

        rec = er.EventRecord(e_list)

        filtered_rec = rec.filter_by_type(e.CustomerServiceEvent)
        assert filtered_rec.get_event_list() == []

    def test_filter_by_type_with_mixed_events(self):
        bank = b.Bank()
        cust = c.Customer(bank)

        e1 = e.CustomerArrivalEvent(1, cust)
        e2 = e.CustomerArrivalEvent(1, cust)
        e3 = e.CustomerDepartureEvent(3, cust)
        e_list = [e1, e2, e3]

        rec = er.EventRecord(e_list)

        filtered_rec = rec.filter_by_type(e.CustomerArrivalEvent)
        assert filtered_rec.get_event_list() == [e1, e2]

