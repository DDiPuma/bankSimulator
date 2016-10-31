# Dominic DiPuma

import sys
sys.path.append("src/")
import main as m
import bank as b

class TestAverageWait:
    def test_one_cust_no_turns(self):
        bank = b.Bank()
        bank.hire_tellers(1)
        bank.customers_arrive(1)

        bank.simulate_tick()

        assert m.get_average_wait_time(bank) == 0

    def test_two_custs(self):
        bank = b.Bank()
        bank.hire_tellers(1)
        bank.customers_arrive(2)

        bank.simulate_tick()
        bank.simulate_tick()

        assert m.get_average_wait_time(bank) == 0.5
