# dict2object
def test1():
    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            # 实现dict
            super(AttrDict, self).__init__(*args, **kwargs)
            # 实现object
            self.__dict__ = self
            #self.__dict__.update(entries)


    args = {'a': 1, 'b': 2}
    o=AttrDict(**args)
    print(o.a, o['a'])

test1()

