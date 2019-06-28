import itertools
import random

from boxx import timeit

with timeit(name="Range"):
    min(random.random() for i in range(100_000))

with timeit(name="Repeat"):
    min(random.random() for _ in itertools.repeat(None, 100_000))
