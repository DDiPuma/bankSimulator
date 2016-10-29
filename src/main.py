# Dominic DiPuma

import bank as b

def main():
    NUM_OF_BANKS = 10

    # Create 10 banks in a list
    banks = [b.Bank() for i in range(NUM_OF_BANKS)]

    # Now hire tellers
    # For each number 1 to 10, get a bank and hire that many tellers
    for i in range(NUM_OF_BANKS):
        banks[i].hire_tellers(i+1)

    # The next step is to send 10 customers to each bank per turn
    # while simulating, for 10 turns
    # Each customer has a service time of 1
    for i in range(10):
        for bank in banks:
            bank.customers_arrive(10, 1)
            bank.simulate_tick()

if __name__ == "__main__":
    main()
