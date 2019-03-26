from struct import unpack
from dis import opmap

reverse_opmap = {v: k for k, v in opmap.items()}


def foo():
    pass


foo_code = foo.__code__.co_code
for pos in range(0, len(foo_code), 2):
    inst = unpack("BB", foo_code[pos : pos + 2])
    print(f"{reverse_opmap[inst[0]]}: {inst[1]}")
