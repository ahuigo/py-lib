class CManager(object):
    def __init__(self):
        print('__init__')

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exception, value, traceback):
        print('__exit__:', exception, "value:",value, "traceback:",traceback)
        return True  # Suppress this exception

    def __del__(self):
        print('__del__', self)

def f():
    with CManager() as c:
        for j in range(3):
            yield j
        print( 'doing something with context:', c)
        raise RuntimeError()
        print ('finished doing something')
    print("end")

for i in f():
    print(i)
