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
    loop_end = True

    def loop(arr):
        nonlocal item
        nonlocal loop_end
        yield item
        old_item = item
        try:
            while True:
                item = next(arr, None)
                if item is None or item[index] != old_item[index]:
                    break
                yield item
        finally:
            loop_end = True
            
    while item is not None and loop_end:
        loop_end = False
        yield loop(arr)

'''
arr = [
    ['dev01', 10],['dev01', 12], ['dev01', 13],
    ['dev01', 21],['dev01', 22], ['dev01', 23],
]

def compare(prev, curr):
    return True if prev[1] - curr[1]>2 else False

for i in iter2reduce(iter(arr), compare):
    for j in i:
        print(j)

'''
def iter2reduce(arr, compare=None, return_end=True):
    item = next(arr, None)
    iter1_end = True

    def iter1(arr):
        nonlocal item
        nonlocal iter1_end
        try:
            while True:
                old_item = item
                item = next(arr, None)
                if item is None or (compare and compare(old_item, item)):
                    if return_end:
                        yield old_item, None
                    break
                yield old_item,item
        finally:
            iter1_end = True
            
    while item is not None and iter1_end:
        iter1_end = False
        #logging.debug(item)
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


