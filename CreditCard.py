class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
    
        customer    the name of the customer (e.g., John Bowman )
        bank        the name of the bank (e.g., California Savings )
        acnt        the acount identifier (e.g., 5391 0375 9387 5309 )
        limit       credit limit (measured in dollars)

        The initial balance is zero.
        """
        self. customer = customer
        self. bank = bank
        self. account = acnt
        self. limit = limit
        self. balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank s name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount