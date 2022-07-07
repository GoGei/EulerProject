"""
https://projecteuler.net/problem=18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
from raw_data import problem_18_data

triangle = problem_18_data[:]

matrix = []
for line in triangle.split('\n'):
    converted = list(map(int, line.split()))
    matrix.append(converted)

for i, line in enumerate(matrix):
    for j in range(len(line)):
        if i == 0 and j == 0:
            continue

        prev_line = matrix[i - 1]
        left = prev_line[j - 1] if j - 1 >= 0 else 0
        right = prev_line[j] if j < len(prev_line) else 0

        matrix[i][j] += max(left, right)

res = max(matrix[-1])
print(res)
ANSWER = 1074
assert ANSWER == res
