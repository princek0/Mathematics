from functools import lru_cache


def factor(n):  # Returns all factors of n in a list.
    d = 2
    factors = []
    while n >= d * d:
        if n % d == 0:
            n = n / d
            factors.append(d)
        else:
            d = d + 1
    if n > 1:
        factors.append(n)
    return factors


@lru_cache(maxsize=5)
def gcd(n, k):  # Returns the greatest common divisor of n and k.
    r = n % k
    if r == 0:
        return k
    else:
        return gcd(n, r)


def lcm(n, k):  # Returns the lowest common multiple of n and k.
    lcm = n * k // gcd(n, k)
    return lcm


def factorial(n):  # Returns the factorial of n.
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


@lru_cache(maxsize=5)
def fibonacci(n):  # Returns the nth fibonacci number.
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def triangular(n):  # Returns the nth triangular number.
    return (n ** 2 + n) / 2



