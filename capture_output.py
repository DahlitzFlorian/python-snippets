import contextlib
import io
import sys


# Option 1
l = io.StringIO()
with contextlib.redirect_stdout(l):
    help(pow)

l = l.getvalue()
print("value:", l)


# Option 2
with open("help.txt", "w") as f:
    with contextlib.redirect_stdout(f):
        help(pow)


# Option 3
with contextlib.redirect_stdout(sys.stderr):
    help(pow)
