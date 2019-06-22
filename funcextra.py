from functools import wraps
import traceback
'''

arr = [
        ['dev01', '1'], ['dev01', '2'], ['dev01', '3'],
        ['dev02', '1'], ['dev02', '2'], ['dev02', '3'],
        ['dev03', '1'], ['dev03', '2'], ['dev03', '3'],
        ]
for i in iter2(iter(arr), 0):
    print(i)
    for j in i:
        print(j)
'''
def iter2(arr, index):
    item = next(arr, None)
    iter1_end = True

    def iter1(arr):
        nonlocal item
        nonlocal iter1_end
        yield item
        old_item = item
        try:
            while True:
                item = next(arr, None)
                if item is None or item[index] != old_item[index]:
                    break
                yield item
        finally:
            iter1_end = True
            
    while item is not None and iter1_end:
        iter1_end = False
        yield iter1(arr)

'''
Retry function/method
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


