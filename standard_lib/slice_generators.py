import itertools


def fibonacci():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, nxt + current
        yield current


first_fove = list(itertools.islice(fibonacci(), 5))
print(f"First five: {first_fove}")
