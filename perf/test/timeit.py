import timeit

str_setup = "str_list = ['some_string' * 2000] * 100"
bytes_setup = "bytes_list = [b'some_bytes' * 2000] * 100"

str_time = timeit.timeit("''.join(str_list)", setup=str_setup, number=10000)
bytes_time = timeit.timeit("b''.join(bytes_list)", setup=bytes_setup, number=10000)

print(f"String join time: {str_time}s")
print(f"Bytes join time: {bytes_time}s")
