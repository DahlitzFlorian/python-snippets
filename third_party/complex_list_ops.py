from blist import blist
from boxx import timeit


def complex_list_ops(x: list) -> list:
    x *= 2**29
    x.append(5)
    y = x[4:-234234]
    del x[3:1024]    
    return x


with timeit(name="Builtin"):
    y = complex_list_ops([0])

with timeit(name="Blist"):
    y = complex_list_ops(blist([0]))
