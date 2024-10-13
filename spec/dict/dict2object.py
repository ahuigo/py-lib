# dict2object
def test1():
    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            # 实现dict
            #super(AttrDict, self).__init__(*args, **kwargs)
            self.update(kwargs)

            # 实现object
            self.__dict__ = self


    args = {'a': 1, 'b': 2}
    o=AttrDict(**args)
    print(o.a, o['a'])
    o.c = 1
    o['d'] = 2
    print(o.c, o['c'])
    print(o.d)

test1()

