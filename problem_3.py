"""
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

target = 600851475143
lim = int(target ** 0.5)
res = 1

for i in range(2, lim):
    if target % i == 0:
        count = 1
        for j in range(2, (i // 2 + 1)):
            if i % j == 0:
                count = 0
                break
        if count == 1 and res <= i:
            res = i

print(res)
ANSWER = 6857
assert ANSWER == res
