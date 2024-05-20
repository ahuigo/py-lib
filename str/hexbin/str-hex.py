import binascii
bytes_hex:str = b'a1'.hex()
print(f"hex:{bytes_hex}")

# convert hex string to bytes
print(f"raw:{binascii.unhexlify(bytes_hex)}")
print(f"raw2:{bytes.fromhex(bytes_hex)}")
