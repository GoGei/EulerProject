"""
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

res = sum(filter(lambda e: e % 3 == 0 or e % 5 == 0, range(1, 1000)))
print(res)

ANSWER = 233168
assert ANSWER == res
