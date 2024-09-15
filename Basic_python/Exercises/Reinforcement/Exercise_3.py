# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, 
# and returns the smallest and largest numbers, in the form of a tuple of length two. 
# Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    try:
        smallest = largest = data[0]
        for n in data[1:]:
            if n < smallest:
                 smallest = n
            elif n > largest:
                largest = n
        return (largest, smallest)
    except ValueError:
        print("Input is an empty sequence.")
    

def minmax(data):
    try:
        smallest, largest = data[0], data[0]
        for num in data:
            smallest = num if num < smallest else smallest
            largest = num if num > largest else largest
        return smallest, largest
    except (ValueError, IndexError):
        print("Input is an empty sequence.")

print(minmax([]))