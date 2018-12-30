import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 20)
        print(f"TRACE: calling {func.__name__}() "
              f"with {args}, {kwargs}")

        original_result = func(*args, **kwargs)

        print(f"TRACE: {func.__name__}() "
              f"returned {original_result!r}")
        print("-" * 20)

        return original_result

    return wrapper


@trace
def greet(name, phrase):
    return f"{name}, {phrase}"


print(greet("Florian", "Nice to see you!"))
