# Dominic DiPuma

import pytest
from unittest.mock import MagicMock

import sys
sys.path.append("src/")
import customer as c
import bank as b
import teller as t

"""Note that although bank and teller are imported, they are mocked where
   their functionality is actually called"""

class TestCustomer:
    def test_id_increments(self):
        sample_bank = b.Bank()
        first_cust = c.Customer(sample_bank)
        second_cust = c.Customer(sample_bank)
        assert second_cust.get_id() == first_cust.get_id() + 1

    def test_arrival_event_published(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        # Ultimately, assert that the event is published to the bank
        assert 1

    def test_arrival_time(self):
        sample_bank = b.Bank()
        sample_bank.get_time = MagicMock(return_value = 1)
        cust = c.Customer(sample_bank)

        assert cust.get_arrival_time() == 1

    def test_teller_event_published(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(sample_teller)
        # Ultimately, assert that the event is published to the bank
        assert 1

    def test_time_reached_teller(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        
        sample_teller = t.Teller()
        sample_bank.get_time = MagicMock(return_value = 2)
        cust.go_to_teller(sample_teller)
        
        assert cust.get_time_reached_teller() == 2

    def test_wait_time(self):
        sample_bank = b.Bank()
        sample_bank.get_time = MagicMock(return_value = 1)
        cust = c.Customer(sample_bank)

        sample_teller = t.Teller()
        sample_bank.get_time = MagicMock(return_value = 2)
        cust.go_to_teller(sample_teller)
        
        assert cust.get_wait_time() == 1

    def test_accept_teller_service(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(sample_teller)
        assert cust.accept_teller_service()

    def test_departure_event_published(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        sample_teller = t.Teller()
        cust.go_to_teller(sample_teller)
        cust.accept_teller_service()
        # Ultimately, assert that the event is published to the bank
        assert 1

    def test_total_time(self):
        sample_bank = b.Bank()
        sample_bank.get_time = MagicMock(return_value = 1)
        cust = c.Customer(sample_bank)

        sample_teller = t.Teller()
        sample_bank.get_time = MagicMock(return_value = 2)
        cust.go_to_teller(sample_teller)

        cust.accept_teller_service()
        assert cust.get_total_time() == 2

    def test_time_reached_teller_blank(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        with pytest.raises(Exception) as exception_info:
            cust.get_time_reached_teller()

    def test_invalid_departure_time(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        with pytest.raises(Exception) as exception_info:
            cust.get_departure_time()

    def test_invalid_wait_time(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        with pytest.raises(Exception) as exception_info:
            cust.get_wait_time()

    def test_invalid_total_time(self):
        sample_bank = b.Bank()
        cust = c.Customer(sample_bank)
        with pytest.raises(Exception) as exception_info:
            cust.get_total_time()

    def test_longer_service_time_false(self):
        sample_bank = b.Bank()
        sample_bank.get_time = MagicMock(return_value = 1)
        cust = c.Customer(sample_bank, 2)
        sample_teller = t.Teller()
        sample_bank.get_time = MagicMock(return_value = 2)
        cust.go_to_teller(sample_teller)
        assert ~cust.accept_teller_service()

    def test_longer_service_time_true(self):
        sample_bank = b.Bank()
        sample_bank.get_time = MagicMock(return_value = 1)
        cust = c.Customer(sample_bank, 2)
        sample_teller = t.Teller()
        sample_bank.get_time = MagicMock(return_value = 2)
        cust.go_to_teller(sample_teller)
        cust.accept_teller_service()
        assert cust.accept_teller_service()
