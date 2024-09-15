class Progression:
    """Iterator producing a generic progression
    
    Default Iterator produces the whole numbers 0,1,2,3...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression"""
        self._current = start
    
    def _advance(self):
        """Update self._current to a new value
        
        This should be overriden by a subclass to customize progression

        By convention, if current is set to None, this designates the end of the progression.
        """

        self._current += 1
    
    def __next__(self):
        """Return the next element or raise an exception"""
        if self._current == None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        """By convention an iterator must return itself"""
        return self
    
    def print_progression(self,n):
        """Print next self values of the progression"""
        print(' '.join(str(next(self)) for j in range(n)))



    