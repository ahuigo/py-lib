import pickle
from typing import NamedTuple
import encry_data_pb2

class EncryData(NamedTuple):
    data: bytes
    sign: bytes

def serialize_with_protobuf(encry_data):
    ed = encry_data_pb2.EncryData()
    ed.data = encry_data.data
    ed.sign = encry_data.sign
    return ed.SerializeToString()

def deserialize_with_protobuf(data):
    ed = encry_data_pb2.EncryData()
    ed.ParseFromString(data)
    return EncryData(ed.data, ed.sign)

# 使用示例
encry_data = EncryData(
    data=b'1\xff',
    sign=b'a\xfb'
)

serialized_data = serialize_with_protobuf(encry_data)
print(serialized_data)  

deserialized_data = deserialize_with_protobuf(serialized_data)
print(deserialized_data)  