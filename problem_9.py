"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

lim = 1000


def get_pythagorean_triplet():
    for c in range(1, int(lim / 2)):
        for b in range(1, c + 1):
            for a in range(1, b + 1):
                if not (a ** 2 + b ** 2 == c ** 2):
                    continue
                if a + b + c == lim:
                    return a * b * c
    return 0


res = get_pythagorean_triplet()
print(res)
ANSWER = 31875000
assert ANSWER == res
