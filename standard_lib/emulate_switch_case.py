import operator


dispatch_dict = {
    "add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.floordiv,
}


def dispatch_func(op, x, y):
    return dispatch_dict.get(op, lambda: None)(x, y)


print(f"dispatch_func('mul', 4, 5) = {dispatch_func('mul', 4, 5)}")
