import contextlib,sys,io
@contextlib.contextmanager
def capture():
    oldout,olderr = sys.stdout, sys.stderr
    try:
        out=[io.StringIO(), io.StringIO()]
        sys.stdout,sys.stderr = out
        yield out
    finally:
        sys.stdout,sys.stderr = oldout, olderr

with capture() as out:
    print('some stdout',end="")
    sys.stderr.write('some stderr')

print("stdout:", out[0].getvalue())
print("stdout:", out[1].getvalue())
