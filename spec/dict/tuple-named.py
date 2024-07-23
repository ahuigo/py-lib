from collections import namedtuple
MyStruct = namedtuple('MyStruct', 'a b d')
s = MyStruct(a=1, b={'c': 2}, d=['hi'])
print(s.a)


