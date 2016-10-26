# Dominic DiPuma

class Teller:
    current_id = 0

    def __init__(self):
        _id = self.__class__.current_id
        self.__class__.current_id += 1

        self._bank = None
        self._current_customer = None

        self._customers_served = 0
        self._turns_idle = 0

    def assign_to_bank(self, bank):
        self._bank = bank

    def has_customer(self):
        if self._current_customer == None:
            return False

        return True

    def take_customer(self, cust):
        if self.has_customer():
            raise Exception('Teller already has a customer!')

        self._current_customer = cust
        cust.go_to_teller(self)

    def release_customer(self):
        self._customers_served += 1
        self._current_customer.leave_bank()
        self._current_customer = None

    def work_one_turn(self):
        if ~self.has_customer():
            self._turns_idle += 1
            return

        can_customer_leave = self._current_customer.accept_teller_service()
        if customer_can_leave:
            self.release_customer()

    def get_customers_served(self):
        return self._customers_served

    def get_turns_idle(self):
        return self._turns_idle

    def get_id(self):
        return self._id
