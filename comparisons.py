a = [1, 2, 3]
b = a
c = list(a)

if __name__ == "__main__":
    print(a is b)
    print(a == b)
    print(a is c)
    print(a == c)
"""
NOTES
- is evaluates to True if two variables point to the same, identical object
- == evaluates to True if two variables if the objects referred to by the variables have the same contents (equality)
- if is evaluates to True, == will always evaluate to True (but not necessarily vice-versa)
"""