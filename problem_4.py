"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

res = 0

for i in range(100, 999):
    for j in range(100, 999):
        current = i*j
        str_repr = str(current)
        if str_repr == str_repr[::-1] and res <= current:
            res = current

print(res)
ANSWER = 906609
assert ANSWER == res
