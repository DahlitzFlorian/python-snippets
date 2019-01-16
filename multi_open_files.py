from contextlib import ExitStack, contextmanager


@contextmanager
def multi_open(paths, mode="r"):
    with ExitStack() as stack:
        yield [stack.enter_context(open(path, mode)) for path in paths]


paths = (f"file_{n}.txt" for n in range(10))

with multi_open(paths, "w") as files:
    for file in files:
        file.write("Enter some text to several files.")
