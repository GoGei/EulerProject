"""
https://projecteuler.net/problem=20
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def divisors(n):
    divs = {1}
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.add(i)
    return divs


def d(n):
    return sum(divisors(n))


amicable_numbers = set()
lim = 10000
for a in range(1, lim):
    b = d(a)
    if d(b) == a and b != a:
        amicable_numbers.add(a)
        amicable_numbers.add(b)

res = sum(amicable_numbers)
print(res)
ANSWER = 31626
assert ANSWER == res
