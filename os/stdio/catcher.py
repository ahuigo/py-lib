import io
import contextlib
import time

stdout = io.StringIO()
stderr = io.StringIO()
with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
    import sys
    print("some stdout")
    sys.stderr.write("some stderr\n")

print("stdout:",stdout.getvalue())
print("stderr:",stderr.getvalue())
