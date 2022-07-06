"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


dividers = set(range(1, 21))
found = False
i = max(dividers)
res = 0
lim = 500000000
while True:
    for j in dividers:
        if i % j != 0:
            found = False
            break
        found = True

    if i % 50_000_000 == 0:
        print('%s is passed' % i)

    if found:
        res = i
        break
    else:
        i += 10
        if i >= lim:
            raise ValueError('limit is reached')

print(res)
ANSWER = 232792560
assert ANSWER == res
