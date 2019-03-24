from boxx import timeit


with timeit(name="f-strings"):
    for i in range(500_000):
        x = 6
        f"{x}"

with timeit(name="str"):
    for i in range(500_000):
        x = 6
        str(x)
