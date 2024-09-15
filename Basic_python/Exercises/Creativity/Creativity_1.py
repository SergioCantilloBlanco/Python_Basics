#  Write a pseudo-code description of a function that reverses a list of n integers,
#  so that the numbers are listed in the opposite order than they were before,
#  and compare this method to an equivalent Python function for doing the same thing.

def reverse_list(data):
    n = len(data)
    for i in range(n // 2):
        data[i], data[n - i - 1] = data[n - i - 1], data[i]
    return data

print(reverse_list([1,2,3,4,5]))
