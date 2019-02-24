import warnings


def deprecated(func):
    """This is a decorator which can be used to wmark functions as deprecated.
    It will result in a warning being emitted when the function is used."""

    def new_func(*args, **kwargs):
        warnings.warn(
            f"Call to deprecated function {func.__name__}.", category=DeprecationWarning
        )

        return func(*args, **kwargs)

    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)

    return new_func


# === Example usages ===


@deprecated
def some_old_function(x, y):
    return x + y


class SomeClass:
    @deprecated
    def some_old_method(self, x, y):
        return x + y


some_old_function(1, 2)
example = SomeClass()
example.some_old_method(1, 2)
