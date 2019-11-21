import copy

# shallow copying (one level deep)
original_list = []
new_list = list(original_list)

original_dict = {}
new_dict = dict(original_dict)

original_set = set()
new_set = set(original_set)

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
ys2 = copy.copy(xs)
zs = copy.deepcopy(xs)  # deep copying (all levels)

xs.append(['new sublist'])
xs[1][0] = 'X'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


a = Point(23, 42)
b = copy.copy(a)


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f'Rectangle({self.topleft!r}, {self.bottomright!r})'


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
drect = copy.deepcopy(rect)
rect.topleft.x = 999

if __name__ == "__main__":
    print(xs)
    print(ys)
    print(zs)
    print(a is b)
    print(rect is srect)
    print(rect.topleft is srect.topleft)
    print(rect)
    print(srect)
    print(drect)
"""
NOTES:
- shallow copies don't clone child components
- deep copies recursively clone child components, clone is fully independent of original (slower)
- use copy module
"""