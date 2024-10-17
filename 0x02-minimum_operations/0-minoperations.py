#!/usr/bin/python3

# divide the number by the smallest possible prime and continuing with the quotient
def minOperations(n: int) -> int :
    """Return minimum number of operations to copy paste n chars"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return sum(factors)
