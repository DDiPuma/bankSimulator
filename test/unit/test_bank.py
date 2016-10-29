# Dominic DiPuma

import pytest
from unittest.mock import MagicMock

import sys
sys.path.append("src/")
import bank as b
import customer as c

class TestBank:
    def test_id_increments(self):
        bank1 = b.Bank()
        bank2 = b.Bank()
        assert bank2.get_id() == bank1.get_id() + 1

    def test_time_ticks(self):
        sample_bank = b.Bank()
        sample_bank.simulate_tick()
        assert sample_bank.get_time() == 1

    def test_no_tellers(self):
        sample_bank = b.Bank()
        assert sample_bank.num_of_tellers() == 0

    def test_hire_one_teller(self):
        sample_bank = b.Bank()
        sample_bank.hire_tellers(1)

        assert sample_bank.num_of_tellers() == 1

    def test_hire_two_tellers(self):
        sample_bank = b.Bank()
        sample_bank.hire_tellers(2)

        assert sample_bank.num_of_tellers() == 2

    def test_empty_queue(self):
        sample_bank = b.Bank()
        
        assert sample_bank.length_of_queue() == 0

    def test_one_in_queue(self):
        sample_bank = b.Bank()
        sample_bank.customers_arrive(1)
        assert sample_bank.length_of_queue() == 1

    def test_two_in_queue(self):
        sample_bank = b.Bank()
        sample_bank.customers_arrive(2)
        assert sample_bank.length_of_queue() == 2

    def test_teller_takes_cust(self):
        sample_bank = b.Bank()
        sample_bank.hire_tellers(1)
        sample_bank.customers_arrive(1)
        sample_bank.simulate_tick()
        assert sample_bank.length_of_queue() == 0
