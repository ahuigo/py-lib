from typing import Self
from typing import Callable, Any, Dict, Optional

from .user import User
# 祖父目录
# from ..user import User
# from ...user import User

class Client:
    n: int = 0
    user: Optional[User] = None

    def __init__(self, *args, **kwargs):
        self.printInitArgs(*args, **kwargs)

    def printInitArgs(self, *args, **kwargs):
        print("args:", args)
        print("kwargs", kwargs)

    def add(self, a: int) -> Self:
        self.n += a
        return self

    def reset(self) -> "Self":
        self.n = 0
        return self

    def setHook(self, hook: Optional[Callable[[int, Any], None]] = None) -> Self:
        self.hook = hook
        return self

    def setUser(self, user: User) -> Self:
        self.user = user
        return self
