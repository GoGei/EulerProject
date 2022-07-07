"""
https://projecteuler.net/problem=8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""
import functools
from raw_data import problem_9_data

raw_matrix = problem_9_data[:]

adjacent_len = 13
res = 0
slices = list(filter(lambda s: len(s) >= adjacent_len, raw_matrix.replace('\n', '').split('0')))


def max_of_slices(value):
    if len(value) == adjacent_len:
        return functools.reduce(lambda a, b: a * b, list(map(int, value)))

    target = 0
    for j in range(len(value) - adjacent_len + 1):
        current = max_of_slices(value[j:j + adjacent_len])
        target = max(current, target)
    return target


for v in slices:
    max_of_slice = max_of_slices(v)
    res = max_of_slice if res <= max_of_slice else res

print(res)
ANSWER = 23514624000
assert ANSWER == res
