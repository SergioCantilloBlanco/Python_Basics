class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance
        
        
        The initial balance is zero.

        Customer the name of the costumer (e.g., "John Bowman")
        bank     the name of the bank (e.g., "Santander")
        acnt     the acount identifier (e.g., "2342 3454 8731 8763")
        limit    credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account= acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
            """Return the name of the customer"""
            return self._customer
    

    def get_bank(self):
            """Return the name of the bank"""
            return self._bank
    
    def get_account(self):
            """Return the identifying number of the account"""
            return self._account
    
    def get_limit(self):
            """Return the current limit"""
            return self._limit
    
    def get_balance(self):
            """Return the current balance"""
            return self._balance

    def charge(self,price):
        """
        Charge given prive to the card, assuming suficcient credit limit.

        Return true if charge was procced; False on the contrary.
        """

        if not isinstance(price, (int, float)):
                raise TypeError("price must be numeric")

        if price + self._balance > self._limit:
            return False
        else:
              self._balance += price
              return True
              
    def make_payment(self, amount):
          
          if not isinstance(amount, (int, float)):
                raise TypeError("Amount must be numeric")
          
          if amount < 0:
                raise ValueError("The payment amount cannot be negative.")

          self._balance -= amount


if __name__ == "__main__":
    pass