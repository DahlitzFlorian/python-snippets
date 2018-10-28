import contextlib
import io
import sys


# Option 1
output_stream = io.StringIO()
with contextlib.redirect_stdout(output_stream):
    help(pow)

output_stream = output_stream.getvalue()
print("value:", output_stream)


# Option 2
with open("help.txt", "w") as f:
    with contextlib.redirect_stdout(f):
        help(pow)


# Option 3
with contextlib.redirect_stdout(sys.stderr):
    help(pow)
