# Write a short Python function that takes a positive integer n
# and returns the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
    return int(sum(k*k for k in range(1,n)))

print(sum_of_squares(5))