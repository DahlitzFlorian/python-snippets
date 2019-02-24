"""Reference: https://medium.com/@alexmaisiura/python-how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code-56be6443d524"""
import sys
import tracemalloc


def main():
    tracemalloc.start()

    data = []
    for p in range(100000):
        data.append(DataItem("Alex", 42, "middle of nowhere"))

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")
    total = sum(stat.size for stat in top_stats)
    print("[With __slots__] Total allocated size: %.1f MB" % (total / (1024 * 1024)))

    tracemalloc.stop()

    tracemalloc.start()

    data = []
    for p in range(100000):
        data.append(DataItemWithoutSlots("Alex", 42, "middle of nowhere"))

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")
    total = sum(stat.size for stat in top_stats)
    print("[Without __slots__] Total allocated size: %.1f MB" % (total / (1024 * 1024)))

    tracemalloc.stop()


class DataItem:
    __slots__ = ["name", "age", "address"]

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class DataItemWithoutSlots:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


def get_size(obj, seen=None):
    # From https://goshippo.com/blog/measure-real-size-any-python-object/
    # Recursively finds size of objects
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, "__dict__"):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])

    return size


if __name__ == "__main__":
    main()
