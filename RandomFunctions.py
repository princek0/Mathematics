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


def gcd(n, k):
    while k:
        n, k = k, n % k
    return n


gcd2 = lambda n, k: n if k == 0 else gcd(k, n % k)


def lcm(n, k):  # Returns the lowest common multiple of n and k.
    lcm = n * k // gcd(n, k)
    return lcm


def factorial(n):  # Returns the factorial of n.
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


factorial2 = lambda n: 1 if n <= 1 else n * factorial2(n - 1)  # Returns the factorial of n.


@lru_cache(maxsize=5)
def fibonacci(n):  # Returns the nth fibonacci number.
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci2 = lambda n: n if n <= 1 else fibonacci2(n - 1) + fibonacci2(n - 2)  # Returns the nth fibonacci number.


def triangular(n):  # Returns the nth triangular number.
    return (n ** 2 + n) / 2
