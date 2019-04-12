from itertools import takewhile
from pathlib import Path


foo = Path("foo")
baz = Path("baz")

common_rel_path = Path(
    *[
        set(i).pop()
        for i in (takewhile(lambda x: x[0] == x[1], zip(foo.parts, baz.parts)))
    ]
)
print(common_rel_path)
