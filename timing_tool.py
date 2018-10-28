"""
Illustrates the usage of boxx.timeit() reveilling the time a certain
code block takes to run.
"""
from boxx import timeit
from time import sleep


with timeit():
    sleep(0.01)

with timeit(name="sleep"):
    sleep(0.1)
