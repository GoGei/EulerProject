"""
https://projecteuler.net/problem=23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

lim = 28123
# lim = 30


def divisors(n):
    divs = {1}
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.add(i)
    return divs


def is_abundant(n):
    return n < sum(divisors(n))


abundants = set()
targets = set()

for i in range(1, lim + 1):
    if is_abundant(i):
        abundants.add(i)
print(abundants)

for i in range(1, lim + 1):
    can_be_written = False
    for elem in abundants:
        if i - elem in abundants:
            can_be_written = True
            continue
    if not can_be_written:
        targets.add(i)
print(targets)

res = sum(targets)
print(res)
ANSWER = 4179871
assert ANSWER == res
