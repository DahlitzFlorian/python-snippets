import pysnooper


@pysnooper.snoop()
def foo():
    a = [x for x in range(100)]
    return [x for x in a if x % 2 == 0]


foo()
