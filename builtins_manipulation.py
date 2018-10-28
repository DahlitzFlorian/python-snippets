_print = print


def print(*args, **kwargs):
    nargs = (*args, "\nNumber of arguments:", len(args))
    _print(*nargs, **kwargs)


print("One", "Two", "Three")
