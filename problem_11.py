"""
https://projecteuler.net/problem=11
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""
import functools
import operator
from raw_data import problem_11_data

raw_matrix = problem_11_data[:]

path_len = 4
matrix = []
for line in raw_matrix.split('\n'):
    converted = list(map(int, line.split()))
    matrix.append(converted)

res = 0
iterating = range(1, path_len + 1)


def current(iterable):
    return functools.reduce(operator.mul, iterable)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        j_plus_cond = j + (path_len + 1) <= len(matrix[0])
        j_minus_cond = j - (path_len + 1) >= 0
        i_plus_cond = i + (path_len + 1) <= len(matrix[0])
        i_minus_cond = i - (path_len + 1) >= 0

        if j_minus_cond:
            curr = current([matrix[i][j - k] for k in iterating])
            res = max(curr, res)
        if j_plus_cond:
            curr = current([matrix[i][j + k] for k in iterating])
            res = max(curr, res)
        if i_minus_cond:
            curr = current([matrix[i - k][j] for k in iterating])
            res = max(curr, res)
        if i_plus_cond:
            curr = current([matrix[i + k][j] for k in iterating])
            res = max(curr, res)

        if j_plus_cond and i_plus_cond:
            curr = current([matrix[i + k][j + k] for k in iterating])
            res = max(curr, res)
        if j_plus_cond and i_minus_cond:
            curr = current([matrix[i - k][j + k] for k in iterating])
            res = max(curr, res)
        if j_minus_cond and i_plus_cond:
            curr = current([matrix[i + k][j - k] for k in iterating])
            res = max(curr, res)
        if j_minus_cond and i_minus_cond:
            curr = current([matrix[i - k][j - k] for k in iterating])
            res = max(curr, res)

print(res)
ANSWER = 70600674
assert ANSWER == res
