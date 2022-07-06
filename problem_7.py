"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math


def is_prime(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a + 1
    return num > 1


counter = 0
determined_prime = 0
current = 0
nth_prime = 10_001
while counter < nth_prime:
    if is_prime(current):
        determined_prime = current
        counter += 1
    current += 1

print(determined_prime)
ANSWER = 104743
assert ANSWER == determined_prime
