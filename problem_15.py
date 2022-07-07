"""
https://projecteuler.net/problem=15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

size = 20 + 1  # starter point got 1 position
grid = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if i == 0 and j == 0:
            grid[i][j] = 1
            continue

        left = grid[i - 1][j] if i - 1 >= 0 else 0
        right = grid[i + 1][j] if i + 1 < size else 0
        upper = grid[i][j - 1] if j - 1 >= 0 else 0
        down = grid[i][j + 1] if j + 1 < size else 0

        grid[i][j] = sum([left, right, upper, down])

res = grid[size - 1][size - 1]
print(res)
ANSWER = 137846528820
assert ANSWER == res
