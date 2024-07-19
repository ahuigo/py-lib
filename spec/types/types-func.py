from typing import Self
from typing import Callable, Any, Dict, Optional


class User:
    name: str = "name"
    age: int = 10

    def __str__(self):
        return f"name:{self.name},age:{self.age}"


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


# test types
c = Client().add(1).reset().add(2).add(3)
u = User()
u.age = 20
print(u, c.n)
