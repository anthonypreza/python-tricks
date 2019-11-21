class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # always define this, __str__ falls back on it
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})'

    def __str__(self):
        return f'a {self.color} car'


"""
NOTES:
- control to-string conversion with __str__ and __repr__ dunder methods
- __str__ should be readable, __repr__ should be unambiguous
- always add __repr__ to classes
- __unicode__ instead of __str__ in py2
"""