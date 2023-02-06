"""
Avoid recursion limit with tail-recursive algorithms

Source: http://www.usrsb.in/Bouncing-Python-s-Generators-With-A-Trampoline.html
"""

import types


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g


# Example of a tail-recursive algorithm (last statement is a recursive call)
def fib(count, cur=0, next_=1):
    if count <= 1:
        yield cur
    else:
        yield fib(count - 1, next_, cur + next_)


if __name__ == "__main__":
    print(tramp(fib, 100_000))
