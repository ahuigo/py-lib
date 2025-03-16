class CManager(object):
    def __init__(self):
        print('__init__')

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exception, value, traceback):
        print('__exit__:', exception, "value:",value, "traceback:",traceback)
        return False  # raise exception

    def __del__(self):
        print('__del__', self)

def divide(a:int, b:int):
    with CManager() as ctx:
        return a/b

assert divide(10,5)==2
try:
    divide(1,0)
except Exception as e:
    assert isinstance(e, ZeroDivisionError)
