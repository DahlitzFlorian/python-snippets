import sys

from itertools import repeat


lots_of_fours = repeat(4, times=100_000_000)
print(f"Using itertools.repeat: {sys.getsizeof(lots_of_fours)} bytes")

lots_of_fours = [4] * 100_000_000
print(f"Using list with 100.000.000 elements: {sys.getsizeof(lots_of_fours) / (1024**2)} MB")
