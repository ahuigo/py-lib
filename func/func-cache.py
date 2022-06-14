from functools import lru_cache
import time
  
'''
    LRUCache(Least Recently Used (LRU) cache implementation.) (provided)
    LFUCache(Least Frequently Used (LFU) cache implementation.)
    RRCache(Random Replacement (RR) cache implementation.)
    TTLCache(LRU Cache implementation with per-item time-to-live (TTL) value.)
'''
# Function that computes Fibonacci
@lru_cache(maxsize = 128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
      
n=fib(30)
print(n)
