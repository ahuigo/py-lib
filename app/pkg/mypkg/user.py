class User:
    name: str = "name"
    age: int = 10

    def __str__(self):
        return f"name:{self.name},age:{self.age}"

