# Dominic DiPuma

import sys
sys.path.append("src/")
import customer

class TestCustomer:
    def test_first_customer_id(self):
        first_cust = customer.Customer()
        assert first_cust.get_id() == 0

    def test_second_customer_id(self):
        second_cust = customer.Customer()
        assert second_cust.get_id() == 1 
