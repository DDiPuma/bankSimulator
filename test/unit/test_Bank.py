# Dominic DiPuma

import pytest

import sys
sys.path.append("src/")
from Bank import *

class TestBank:
    def test_time_ticks(self):
        bank = Bank()
        bank.simulate_tick()
        assert bank.get_time() == 1
