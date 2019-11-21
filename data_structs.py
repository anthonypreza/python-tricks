from collections import namedtuple
from typing import NamedTuple
from struct import Struct
from types import SimpleNamespace

Car = namedtuple('Car', 'color mileage automatic')
car1 = Car('red', 3000.0, True)


class Car2(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car2 = Car('red', 3000.0, True)

# struct.Struct converts between python values and C structs serialized into Python bytes objects
# can be used to handle binary data stored in files/from network connections
# data exchange format
MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)

car3 = SimpleNamespace(color='red',
                       mileage=3812.4,
                       automatic=True)
car3.mileage = 12
car3.windshield = 'broken'
del car3.automatic

if __name__ == "__main__":
    print(car1)
    print(car1.mileage)
    print(car2)
    print(data)
    print(MyStruct.unpack(data))
    print(car3)
    print(car3.mileage)
