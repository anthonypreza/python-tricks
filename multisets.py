from collections import Counter

# set is unordered collection of objects that does not allow duplicate elements
# quickly test a value for membership in the set, insert or delete new values from a set, compute union/intersection
vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x * x for x in range(10)}
print('e' in vowels)
letters = set('alice')
print(letters)
print(letters.intersection(vowels))
vowels.add('x')
print(vowels)
print(len(vowels))

# immutable set, hashable and can be used as keys or elements of another set
vowels = frozenset('aeiou')
print(vowels)
d = {frozenset([1, 2, 3]): 'hello'}
print(d[frozenset({1, 2, 3})])
inventory = Counter()
loot = {'sword': 1,
        'bread': 3}
inventory.update(loot)
print(inventory)
more_loot = {'sword': 1,
             'apple': 1}

inventory.update(more_loot)
print(inventory)
print(len(inventory))
print(sum(inventory.values()))
