"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


lim = 2_000_000
res = sum(filter(lambda e: is_prime(e), range(2, lim)))
print(res)

ANSWER = 142913828922
assert ANSWER == res
