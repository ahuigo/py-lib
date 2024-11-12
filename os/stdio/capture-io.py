import io
import contextlib
import time

stdout = io.StringIO()
stderr = io.StringIO()
#　多个上下文同时生效
with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
    import sys
    print("some stdout")
    sys.stderr.write("some stderr\n")

print("stdout:",stdout.getvalue())
print("stderr:",stderr.getvalue())
