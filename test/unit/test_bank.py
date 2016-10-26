# Dominic DiPuma

import sys
sys.path.append("src/")
import bank as b

class TestBank:
    def test_time_ticks(self):
        sampleBank = b.Bank()
        sampleBank.simulate_tick()
        assert sampleBank.get_time() == 1
