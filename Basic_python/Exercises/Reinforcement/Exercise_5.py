# Write a short Python function that takes a positive integer n 
# and returns the sum of the squares of all the odd positive integers smaller than n.

def sum_of_squares_odd(n):
    return int(sum(k*k for k in range(1,n) if k%2 == 1))

print(sum_of_squares_odd(5))