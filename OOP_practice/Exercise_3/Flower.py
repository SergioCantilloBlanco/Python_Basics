class Flower:
    """Object identified as a flower"""

    def __init__(self, name: str, number_petals: int, price: float):
        """Initialize an instance of a flower"""

        self._name = name
        self._number_petals = number_petals
        self._price = price

    def get_name(self):
        return self._name
    
    def get_number_petals(self):
        return self._number_petals
    
    def get_price(self):
        return self._price
    
    def set_name(self, name: str):
        self._name = name
    
    def set_number_petals(self, number_petals: int):
        self._number_petals = number_petals
    
    def set_price(self, price:float):
        self._price = price
    


