'''
DESCRIPTION:

A twin prime is a prime number that is either 2 less or 2 more than another prime number—for example, either member of the twin prime pair (41, 43). In other words, a twin prime is a prime that has a prime gap of two. Sometimes the term twin prime is used for a pair of twin primes; an alternative name for this is prime twin or prime pair. (from wiki https://en.wikipedia.org/wiki/Twin_prime)

Your mission, should you choose to accept it, is to write a function that counts the number of sets of twin primes from 1 to n.

If n is wrapped by twin primes (n-1 == prime && n+1 == prime) then that should also count even though n+1 is outside the range.

Ex n = 10

Twin Primes are (3,5) (5,7) so your function should return 2!
'''

def twin_prime(n):
    if n <= 2:
        return 0
    a = list(range(2, n + 2))
    b = []
    for p in range(2, n + 2):
        if a[p - 2] != 0:
            b.append(a[p - 2])
            if p * p < n + 1:
                for q in range(p * p, n + 2):
                    if q % p == 0:
                        a[q - 2] = 0
    s = len(b)
    i = 0
    sum = 0
    while i < s - 1:
        if b[i + 1] == b[i] + 2:
            sum += 1
        i += 1
    return sum
