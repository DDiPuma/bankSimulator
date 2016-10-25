# Dominic DiPuma

import sys
sys.path.append("src/")
from bank import Bank

class TestBank:
    def test_time_ticks(self):
        bank = Bank()
        bank.simulate_tick()
        assert bank.get_time() == 1
