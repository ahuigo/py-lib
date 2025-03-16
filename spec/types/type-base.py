# Union
## >py3.9
def process_value(val: str | float | int | bool):
    pass


## <=py3.9
from typing import Union
def process_value(val: Union[str, float, int, bool]):
    # Your code here
    pass


# List
from typing import List,Self
names: List[str] = []

