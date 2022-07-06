"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

lim = 100
values = range(1, lim+1)
sum_of_squares = sum((x**2 for x in values))
square_of_sum = sum(values) ** 2
res = square_of_sum - sum_of_squares
print(res)

ANSWER = 25164150
assert ANSWER == res
