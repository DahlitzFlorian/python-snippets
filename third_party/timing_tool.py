from boxx import timeit
from time import sleep


with timeit():
    sleep(0.01)

with timeit(name="sleep"):
    sleep(0.1)
