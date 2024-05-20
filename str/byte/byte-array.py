'''
1. bytes 是不可变的（immutable），这意味着一旦创建了 bytes 对象，就不能更改它的内容。
    你不能b=b'a'; b[0]=98
2. bytearray 是可变的（mutable），这意味着你可以修改 bytearray 对象的内容，
    所以它有一些 bytes 没有的方法，例如 append、remove 和 reverse 等。

由于bytes、bytearray 和 memoryview  有相同的接口方法,所以作为函数参数时,它们基本可以互相替代
'''
d= bytearray()
d+=b'hello'
d[0]=0x41

print(d.decode())
