"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import num2words

res = 0
lim = 1000
for i in range(1, lim+1):
    number_str = num2words.num2words(i)
    cleaned = number_str.replace(' ', '').replace(',', '').replace('-', '')
    res += len(cleaned)

print(res)
ANSWER = 21124
assert ANSWER == res
