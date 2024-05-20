import pickle
from typing import NamedTuple
class EncryData(NamedTuple):
    data: bytes
    sign: bytes

def serialize_with_pickle(encry_data):
    return pickle.dumps(encry_data)

def deserialize_with_pickle(pickled_data):
    return pickle.loads(pickled_data)

# 使用示例
encry_data = EncryData(
    data=b'1\xff',
    sign=b'a\xfb'
)

# pickle模块的安全性不如JSON，因为它可以序列化和反序列化任何Python对象，包括执行代码的对象
pickled_data = serialize_with_pickle(encry_data)
print(pickled_data)  

deserialized_data = deserialize_with_pickle(pickled_data)
print("output:", deserialized_data)  