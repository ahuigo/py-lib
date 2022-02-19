import sys,functools
@functools.lru_cache(maxsize=None) # default maxsize=128
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print(fib(10))
