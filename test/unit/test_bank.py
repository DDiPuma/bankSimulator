# Dominic DiPuma

import sys
sys.path.append("src/")
import bank 

class TestBank:
    def test_time_ticks(self):
        sampleBank = bank.Bank()
        sampleBank.simulate_tick()
        assert sampleBank.get_time() == 1
