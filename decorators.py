import functools


def null_decorator(func):
    return func


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def hello():
    """Return a friendly greeting."""
    return 'hello world'


def strong(func):
    @functools.wraps(func)
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    @functools.wraps(func)
    def wrapper():
        return '<em>' + func() + '</em>'

    return wrapper


@strong
@emphasis
def greet():
    return 'Hello!'


def proxy(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__} returned {original_result!r}')
        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


if __name__ == "__main__":
    print(hello())
    print(greet())
    print(say('Jane', 'Hello'))
    print(hello.__name__, hello.__doc__)
"""
NOTES:
- decorators define reusable building blocks you can apply to a callable to modify its behavior
- @ syntax is shorthand for calling the decorator on input function
- decorators stack from bottom to top
- use functools.wraps helper in decorators to carry over metadata
"""