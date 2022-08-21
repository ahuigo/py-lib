from functools import wraps
import traceback
'''
Retry function/method

@retry(3,True)
def get()
'''
def retry(howmany=2, raiseError=True):
    def tryIt(func):
        @wraps(func)
        def f(*args,**kw):
            attempts = 0
            while attempts < howmany:
                try:
                    return func(*args, **kw)
                except Exception as e:
                    print(traceback.format_exc())
                    attempts += 1
                    if raiseError and attempts == howmany:
                        raise e

        return f
    return tryIt



'''
分组迭代:
example 1:

    arr = [
            ['dev01', '1'], ['dev01', '2'], ['dev01', '3'],
            ['dev02', '1'], ['dev02', '2'], ['dev02', '3'],
            ['dev03', '1'], ['dev03', '2'], ['dev03', '3'],
            ]
    for i in iterChunk(iter(arr), 0):
        print(i)
        for j in i:
            print(j)


example 2:

    arr = [
        ['dev01', '10'],['dev01', '12'], ['dev01', '13'],
        ['dev01', '21'],['dev01', '22'], ['dev01', '23'],
    ]

    def compare(prev, curr):
        return curr[1][0]!=prev[1][0]

    for i in iterChunk(iter(arr), compare=compare):
        print(i)
        for j in i:
            print(j)

'''
def iterChunk(arr, index=None, compare = None):
    item = next(arr, None)
    iter1_end = True

    def iter1(arr):
        nonlocal item
        nonlocal iter1_end
        try:
            while True:
                yield item
                old_item = item
                item = next(arr, None)
                if item is None \
                    or (index is not None and item[index] != old_item[index]) \
                    or (compare and compare(old_item, item)):
                    break
        finally:
            iter1_end = True
            
    while item is not None and iter1_end:
        iter1_end = False
        yield iter1(arr)

'''
chunk via step
'''
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

'''
也可以用: groupby
    from itertools import groupby, count
'''
from itertools import groupby, count
def chunks(iterable, size=10):
    c = count()
    for _, g in groupby(iterable, lambda _: next(c)//size):
        yield g

if True:
    s = range(12)
    for chunk in chunks(s,5):
        print(chunk)
        print(list(chunk))

'''
配对迭代
'''
def iterReduce(arr, return_end=True):
    item = next(arr, None)
    if item is None:
        return

    while True:
        old_item = item
        item = next(arr, None)
        if item is None:
            if return_end:
                yield old_item, None
            break
        yield old_item,item
            
