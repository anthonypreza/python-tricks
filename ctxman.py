from time import time
import threading
from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)


class Timer:
    def __init__(self):
        self.start = time()

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        self.diff = self.end - self.start
        print(f'Execution time: {self.diff} s')


@contextmanager
def timer():
    try:
        start = time()
        yield start
    finally:
        end = time()
        diff = end - start
        print(f'Execution time: {diff} s')


if __name__ == "__main__":
    with open("hello.txt", "w") as f:
        f.write("hello, world!")

    f = open("hello.txt", "w")
    try:
        f.write('hello, world!')
    finally:
        f.close()

    some_lock = threading.Lock()

    with some_lock:
        print('Doing something...')

    with ManagedFile('hello_managed.txt') as f:
        f.write('hello world!\n')
        f.write('bye now')

    with managed_file('hello_managed2.txt') as f:
        f.write('hello world!\n')
        f.write('bye now')

    print('start')
    with Indenter() as indent:
        indent.print('hi')
        with indent:
            indent.print('hello')
            with indent:
                indent.print('bonjour')
            indent.print('hey')

    with Timer():
        with Indenter() as indent:
            indent.print('hi')
            with indent:
                indent.print('hello')
                with indent:
                    indent.print('bonjour')
                indent.print('hey')

    with timer():
        with Indenter() as indent:
            indent.print('hi')
            with indent:
                indent.print('hello')
                with indent:
                    indent.print('bonjour')
                indent.print('hey')
"""
NOTES:
- with statement simplifies exception handling by encapsulating standard uses of try/finally
- manage safe acquisition and release of system resources
- avoid resource leaks and make easier to read code
"""