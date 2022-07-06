"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def next_number(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1


def chain_gen(n):
    counter = 1
    res = n
    while res != 1:
        res = next_number(res)
        counter += 1
    return counter


target, chain_len = 0, 0
lim = 1_000_000
for i in range(1, lim + 1):
    curren_len = chain_gen(i)
    if curren_len >= chain_len:
        chain_len = curren_len
        target = i

print(target)
ANSWER = 837799
assert ANSWER == target
