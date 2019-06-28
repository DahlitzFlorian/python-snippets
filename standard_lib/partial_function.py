from functools import partial
from itertools import repeat

times = partial(repeat, None)
min(random.random() for _ in times(100_000))
