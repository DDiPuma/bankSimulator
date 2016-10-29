# Dominic DiPuma

import pytest
from unittest.mock import MagicMock

import sys
sys.path.append("src/")
import teller as t
import bank as b
import customer as c

"""While bank and customer are imported, any functional dependencies are
   mocked out"""

class TestTeller:
    def test_id_increments(self):
        first_teller = t.Teller()
        second_teller = t.Teller()
        assert second_teller.get_id() == first_teller.get_id() + 1

    def test_take_customer(self):
        sample_teller = t.Teller()
        sample_bank = b.Bank()
        sample_cust = c.Customer(sample_bank)

        sample_cust.go_to_teller = MagicMock(return_value=1)

        sample_teller.take_customer(sample_cust)

        assert sample_cust.go_to_teller.called

    def test_take_two_customers(self):
        sample_teller = t.Teller()
        sample_bank = b.Bank()

        sample_cust1 = c.Customer(sample_bank)
        sample_cust2 = c.Customer(sample_bank)

        sample_teller.take_customer(sample_cust1)
        with pytest.raises(Exception) as exception_info:
            sample_teller.take_customer(sample_cust2)

    def test_service_customer_with_one_turn_once(self):
        sample_teller = t.Teller()
        sample_bank = b.Bank()
        sample_cust = c.Customer(sample_bank)

        sample_teller.take_customer(sample_cust)
        sample_teller.work_one_turn()

        assert ~sample_teller.has_customer()

    def test_service_customer_with_two_turns_once(self):
        sample_teller = t.Teller()
        sample_bank = b.Bank()
        sample_cust = c.Customer(sample_bank, 2)

        sample_teller.take_customer(sample_cust)
        sample_teller.work_one_turn()

        assert sample_teller.has_customer()

    def test_service_customer_with_two_turns_twice(self):
        sample_teller = t.Teller()
        sample_bank = b.Bank()
        sample_cust = c.Customer(sample_bank, 2)

        sample_teller.take_customer(sample_cust)
        sample_teller.work_one_turn()
        sample_teller.work_one_turn()

        assert ~sample_teller.has_customer()
