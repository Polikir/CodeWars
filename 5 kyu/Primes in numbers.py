'''

DESCRIPTION:

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

'''


import math
def primeFactors(n):

    o = []
    ser = math.floor(math.sqrt(n))
    d = dict({})
    x = 2
    while n > 1:
        while n % x == 0 and n > 1:
            d[x] = d.get(x, 0) + 1
            n //= x
        x += 1
    for x in d:
        if d[x] >1:
            o.append(f'({x}**{d[x]})')
        else:
            o.append(f'({x})')
    return ''.join(o)