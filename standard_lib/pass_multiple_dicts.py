from collections import ChainMap


def f(a, b, c, d):
    print(a, b, c, d)


d1 = dict(a=5, b=6)
d2 = dict(b=7, c=8, d=9)

# The old may without overwriting previous values
f(**ChainMap(d1, d2))

# Since Python 3.5 allowing value overwriting
f(**{**d1, **d2})

