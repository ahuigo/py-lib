import sys, os
print( "name:" + __name__, "package:", __package__, "cwd:" + os.getcwd(), "sys.path:", sys.path[0:2],)
from mypkg.client import Client


# 关于sys.path 参考 readme.md
def test_client():
    client = Client("arg1", "arg2")
    n = client.add(2).add(3).n
    assert n == 7, "expect 5"

if __name__ == "__main__":
    test_client()
