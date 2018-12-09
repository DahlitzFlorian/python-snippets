"""The original functions metadata are lost when using a decorator.
Keep them using functools.wraps"""
from functools import wraps


def tags(tag_name):
    """Wraps another function"""

    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return f"<{tag_name}>{func(name)}</{tag_name}>"

        return func_wrapper

    return tags_decorator


@tags("p")
def get_text(name):
    """Returns some text"""
    return "Hello " + name


print(get_text("World"))

print(get_text.__name__)
print(get_text.__doc__)
