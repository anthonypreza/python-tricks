def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


def foobar(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    foo(x, *new_args, **kwargs)


def print_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')


if __name__ == "__main__":
    foo('hello', 1, 2, 3, key1='value', key2=999)
    foobar('hello', 1, 2, 3, key1='value', key2=999)

    tup_vec = (3, 2, 1)
    list_vec = [2, 1, 3]
    print_vector(1, 2, 3)
    print_vector(tup_vec[0], tup_vec[1], tup_vec[2])
    print_vector(*list_vec)

    genexpr = (x * x for x in range(3))
    print_vector(*genexpr)

    dict_vec = {'y': 0, 'z': 1, 'x': 1}
    print_vector(**dict_vec)
"""
NOTES:
- *args and **kwargs let you write functions with a variable number of arguments
- *args -> tuple, **kwargs -> dict
- args and kwargs is a convention you should stick to
- putting * before an iterable in a function call will unpack it and pass elements as separate positional arguments
"""
