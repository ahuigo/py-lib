# pkg import　demo
> refer post/py/py-pkg-import.md

## create pkg

    make create

## python执行时的sys.path
默认python ./path/to/a.py时, sys.path 只会加`./path/to`.
将.添加到sys.path的几种方法如下:
1. python -m mod 执行时，sys.path 会自动的添加`.` 目录，python3 -m pytest也一样
2. alias p='PYTHONPATH=. python a.py'　相当于 `if __name__ == "__main__": sys.path.append(".")`

### 执行时, `__name__==__main__`:
以tests/test_client.py 为例

    # 1. 以`python -m` 执行时，cwd目录会自动被添加到`sys.path[0]` 
    # ok: sys.path[0] 是 ./
    python -m tests.test_client
        cwd:./ sys.path0:./

    # 2. 以`python ./tests/a.py` 执行时，./tests/ 目录添加到`sys.path[0]`
    # fail：No module named 'mypkg', sys.path0 是./tests/
    python tests/test_client.py
        cwd:./ sys.path0:./tests

    # 3. 手动添加当前目录到sys.path
    # ok: like sys.path.append('.'), sys.path 为./tests + ./
    PYTHONPATH=. python tests/test_client.py

### 执行时, `__name__==tests.test_client`:

    # ok: 以python -m执行
    make test
    python3 -m pytest -s

## import relation path
run at root:


run at /test:
