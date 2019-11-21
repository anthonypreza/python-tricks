"""Dictionaries"""
from array import array
from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType

# dict (maps, hashmaps, lookup tables, associative array)
# keys are hashable (hash value never changes, can be compared to other objects)

phonebook = {
    'bob': 7387,
    'alice': 3719,
    'jack': 7052,
}

squares = {x: x * x for x in range(6)}

# OrderedDict - remember the insertion order of keys
d = OrderedDict(one=1, two=2, three=3)
d['four'] = 4

# defaultdict - initalize empty keys with default factory
dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')

# ChainMap - search multiple dicts as a single mapping
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)

# MappingProxyType - wrapper for making read-only dictionaries
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
"""---"""

"""Arrays"""
# fixed-size data records efficiently located based on index
# contiguous data structure (store info in adjoining blocks of memory)
# typed array only allows elements of the same type
# list (dynamic array)

arr = ['one', 'two', 'three']

# tuple (immutable container)
tup = 'one', 'two', 'three'

float_array = array('f', (1.0, 1.5, 2.0, 2.5))
"""---"""

"""Strings"""
# recursive data structures representing a sequence of characters
word = 'abcd'
"""---"""

"""Bytes"""
# immutable sequences of single bytes (0 <= x <= 255)
# immutable arrays of bytes
# dedicated mutable byte array called a bytearray
b = bytes((0, 1, 2, 3))
b_arr = bytearray((0, 1, 2, 3))

if __name__ == "__main__":
    # dict
    print(phonebook['alice'])
    print(squares)
    print(d.keys())
    print(dd['dogs'])
    print(chain)
    print(chain['three'])
    print(chain['one'])
    # print(chain['missing'])
    print(read_only['one'])
    # read_only['two'] = 3  # doesn't work
    writable['one'] = 42  # updates are reflected in proxy
    print(read_only['one'])
    # array
    print(arr)
    print(arr[0])
    arr[1] = 'hello'
    print(arr)
    del arr[1]
    print(arr)
    arr.append(23)
    print(arr)
    print(tup)
    print(tup[0])
    # tup[1] = 'hello'  # doesn't work
    print(tup + (23,))  # creates a copy of the element
    print(float_array[1])
    print(float_array)
    float_array[1] = 23.0
    print(float_array)
    del float_array[1]
    print(float_array)
    float_array.append(42.0)
    print(float_array)
    print(word[1])
    print(word)
    # word[1] = 'e' # doesn't work
    # del word[1] # doesn't work
    print(list(word))
    print(''.join(list('abcd')))
    print(b[1])
    print(b)
    # b[1] = 23 # doesn't work
    print(b_arr[1])
    print(b_arr)
    b_arr[1] = 23
    print(b_arr[1])
    del b_arr[1]
    b_arr.append(42)
    print(b_arr)
    print(bytes(b_arr))