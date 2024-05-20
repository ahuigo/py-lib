import zlib

data = b'hello hello'

edata = zlib.compress(data)
print(zlib.decompress(edata))
