import json
from abc import ABCMeta, abstractmethod
from collections import namedtuple

# class Base:
#     def foo(self):
#         raise NotImplementedError()

#     def bar(self):
#         raise NotImplementedError()


# class Concrete(Base):
#     def foo(self):
#         return 'foo() called'


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass


Car = namedtuple('Car', ['color', 'mileage'])


class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


if __name__ == "__main__":
    # b = Base()
    # b.foo()
    assert issubclass(Concrete, Base)
    # c = Concrete()
    # c.foo()
    # c.bar()

    my_car = MyCarWithMethods('red', 3812.4)
    print(my_car.color)
    print(my_car[0])
    color, mileage = my_car
    print(color, mileage)
    print(*my_car)
    print(my_car.hexcolor())
    print(json.dumps(my_car._asdict()))
