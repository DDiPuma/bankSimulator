# Dominic DiPuma

class Teller:
    """The teller holds a customer, provides them service, and releases them.
    The Bank class should be responsible for generating Tellers as well as
    handing them customers and ordering them to work, via the has_customer,
    take_customer, and work_one_turn methods.
    It tracks its customers served and turns idle as well.  These
    pieces of data are unused as of yet, but provide (tested!) functionality
    if the customers' use cases expand in the future"""

    # ID is a class attribute, and constructs identifiable tellers for printing
    # purposes in the future
    current_id = 0

    def __init__(self):
        # Constructor takes no arguments
        self._id = self.__class__.current_id
        self.__class__.current_id += 1

        self._current_customer = None
        self._customers_served = 0
        self._turns_idle = 0

    def has_customer(self):
        # Returns a boolean of whether or not the teller already has a customer
        # Works on the Python principle that None is false-y
        # But requires devs to be careful to clear out the customer when the
        # customer leaves the teller (this is unit tested)
        if self._current_customer:
            return True

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

    def release_customer(self):
        # Track data, make the customer leave the bank, and clear the teller's
        # customer attribute
        self._customers_served += 1
        self._current_customer.leave_bank()
        self._current_customer = None

    def work_one_turn(self):
        # If there is a customer at the teller, service them
        if self.has_customer():
            # The customer should leave the teller if they have reached their
            # maximum needed turns for service
            customer_can_leave = self._current_customer.accept_teller_service()
            if customer_can_leave:
                self.release_customer()
        # If the teller is idling, track that data
        else:
            self._turns_idle += 1
            return

    # Below this point are all dumb getter methods
    def get_customers_served(self):
        return self._customers_served

    def get_turns_idle(self):
        return self._turns_idle

    def get_id(self):
        return self._id
