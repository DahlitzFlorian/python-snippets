import time

from contextlib import contextmanager


@contextmanager
def timing(description: str):
    start = time.time()
    yield
    print(f"{description}: {time.time() - start}")


with timing("Time List Comprehension"):
    s = [x for x in range(10_000_000)]
