# Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. 
# The random module includes a more basic function randrange, with parameterization similar to the built-in range function, 
# that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.

import random

def custom_choice(data):
    index = random.randrange(len(data))
    return data[index]
