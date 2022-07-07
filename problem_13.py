"""
https://projecteuler.net/problem=13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
from raw_data import problem_13_data
raw_string = problem_13_data[:]

target = 10
summ = sum(map(int, (e for e in raw_string.split('\n'))))
res = str(summ)[:target]
print(res)
ANSWER = '5537376230'
assert ANSWER == res
