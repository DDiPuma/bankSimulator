# Dominic DiPuma

class TestCustomer:
    def test_first_customer_id(self):
        first_cust = Customer()
        assert first_cust.get_id() == 1

    def test_second_customer_id(self):
        first_cust = Customer()
        second_cust = Customer()
        assert second_cust.get_id() == 2
