def yell(text):
    return text.upper() + '!!!'


bark = yell

# del yell

funcs = [bark, str.lower, str.capitalize]


def greet(func):
    greeting = func('Hi, I\'m a program')
    print(greeting)


def get_speak_func(text, vol):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if vol > 0.5:
        return yell
    return whisper


def make_adder(n):
    def add(x):
        return x + n

    return add


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


def make_lambda_adder(n):
    return lambda x: x + n


if __name__ == "__main__":
    print(yell('hello'))
    print(bark('woof'))
    print(bark.__name__)
    print([f('hey there') for f in funcs])
    print(funcs[0]('heyho'))
    print(greet(bark))
    print(list(map(bark, ['hello', 'hey', 'hi'])))
    print(get_speak_func('hello', 0.3)())
    print(get_speak_func('hey', 0.7)())
    plus_3 = make_adder(3)
    plus_5 = make_adder(5)
    print(plus_3(4))
    print(plus_5(4))
    plus_10 = Adder(10)
    print(plus_10(4))
    print(callable(plus_10))
    plus_20 = make_lambda_adder(20)
    print(plus_20(10))
"""
NOTES:
- all things in Python are objects, including functions
- can assign functions to variables, store in data structures, pass and return them
- first-class functions allow you to pass around behavior in programs
- functions can be nested and child functions can carry parent function state (closures)
- objects can be made callable (treat object like function)
- lambdas should be used sparingly and with extraordinary care
"""