from Progression import *


class ArithmeticProgression(Progression):                       #inherit fron Progression
    """Iterator producing an arithmetic progression"""


    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.
        
        
        Increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)
        
        """
        super().__init__(start)                 #Initialize base class
        self._increment = increment

    def _advance(self):                         #Override inherited version
        """Update current value by adding the fixed increment"""
        self._current += self._increment 

