'''
在这个函数的返回类型 Generator[LiteralString | str, Any, None] 中：
LiteralString | str 是生成器产生的值的类型。这表示生成器可以产生 LiteralString 类型或 str 类型的值。
Any 是生成器接收的值的类型。这表示你可以发送任何类型的值给生成器（使用 generator.send(value) 方法）。
'''
def getQuery()->Generator[LiteralString | str, Any, None]:
    query = 'abc '
    query = query.strip()
    yield query
