from typing import TypeVar, Generic

T = TypeVar('T')
def unwrap(val: T | None) -> T:
    assert val is not None
    return val
