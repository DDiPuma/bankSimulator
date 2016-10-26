# Dominic DiPuma

import pytest

import sys
sys.path.append("src/")
import customer as c
import bank as b
import teller as t

class TestCustomer:
    def test_first_customer_id(self):
        first_cust = c.Customer()
        assert first_cust.get_id() == 0

    def test_second_customer_id(self):
        second_cust = c.Customer()
        assert second_cust.get_id() == 1 

    def test_bank_arrival(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        # Ultimately, assert that the event is published to the bank
        assert 1

    def test_arrival_time(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        assert cust.get_arrival_time() == 1

    def test_go_to_teller(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        # Ultimately, assert that the event is published to the bank
        assert 1

    def test_time_reached_teller(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        assert cust.get_time_reached_teller() == 2

    def test__wait_time(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        assert cust.get_wait_time() == 1

    def test_accept_teller_service(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        assert cust.accept_teller_service()

    def test_leave_bank_called_by_departure_time_assignment(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        cust.accept_teller_service()
        assert cust.get_departure_time()

    def test_leave_bank_called_by_event_publishing(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        cust.accept_teller_service()
        # Ultimately, assert that the event is published to the bank
        assert 1

    def test_total_time(self):
        sample_bank = b.Bank()
        cust = c.Customer(1)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        cust.accept_teller_service()
        assert cust.get_total_time() == 2

    def test_arrival_time_blank(self):
        cust = c.Customer()
        with pytest.raises(Exception) as exception_info:
            cust.get_arrival_time()

    def test_time_reached_teller_blank(self):
        cust = c.Customer()
        with pytest.raises(Exception) as exception_info:
            cust.get_time_reached_teller()

    def test_invalid_departure_time(self):
        cust = c.Customer()
        with pytest.raises(Exception) as exception_info:
            cust.get_departure_time()

    def test_invalid_wait_time(self):
        cust = c.Customer()
        with pytest.raises(Exception) as exception_info:
            cust.get_wait_time()

    def test_invalid_total_time(self):
        cust = c.Customer()
        with pytest.raises(Exception) as exception_info:
            cust.get_total_time()

    def test_longer_service_time_false(self):
        sample_bank = b.Bank()
        cust = c.Customer(2)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        assert ~cust.accept_teller_service()

    def test_longer_service_time_true(self):
        sample_bank = b.Bank()
        cust = c.Customer(2)
        cust.go_to_bank(1, sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(2, sample_teller)
        cust.accept_teller_service()
        assert cust.accept_teller_service()
