from typing import List, cast,Dict, Any

class SpanMeta:
    pass

o: Dict[int, Any] = {1:  [SpanMeta()]}

# 类型转换断言
a =  cast(List[SpanMeta], o[1])
print(a)
