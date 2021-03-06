# Dominic DiPuma

"""Contains the Teller class"""

class Teller:
    # ID is a class attribute, and constructs identifiable tellers for printing
    # purposes in the future
    current_id = 0

    def __init__(self):
        self._id = self.__class__.current_id
        self.__class__.current_id += 1

        self._current_customer = None

    def has_customer(self):
        # Returns a boolean of whether or not the teller already has a customer
        # But requires devs to be careful to clear out the customer when the
        # customer leaves the teller (this is unit tested)
        if self._current_customer:
            return True
        else:
            return False

    def take_customer(self, cust):
        # Assigns the tellre a customer, and throws an exception if there is
        # a customer already assigned
        # The Bank class should check this before, but the exception provides
        # safety against programmer error
        if self.has_customer():
            raise Exception('Teller already has a customer!')

        self._current_customer = cust
        cust.go_to_teller(self)

    def work_one_turn(self):
        # If there is a customer at the teller, service them
        if self.has_customer():
            # The customer should leave the teller if they have reached their
            # maximum needed turns for service
            customer_can_leave = self._current_customer.accept_teller_service()
            if customer_can_leave:
                self._current_customer = None

    # Below this point are all dumb getter methods
    def get_id(self):
        return self._id
