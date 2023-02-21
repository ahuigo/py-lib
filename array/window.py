from itertools import islice

def iterWindow(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def iterWindow2(seq, n=2):
    for i in range(len(seq) - n + 1):
        yield seq[i: i + n]

'''
配对迭代: 滑动窗口
for prev,curr in iterWindow3(iter(arr)):
'''
def iterWindow3(arr, return_end=False):
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
            
