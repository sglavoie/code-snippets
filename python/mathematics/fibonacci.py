def fib_seq(x):
    """Fibonacci sequence, recursively."""
    if x == 0:
        return 0
    if x == 1:
        return 1
    x = fib_seq(x - 1) + fib_seq(x - 2)
    return x


def fib_efficient(n, fib_dict=None):
    """Recursive version storing intermediate values along the way."""
    if fib_dict is None:
        fib_dict = {1: 1, 2: 2}
    if n in fib_dict:
        return fib_dict[n]

    ans = fib_efficient(n - 1, fib_dict) + fib_efficient(n - 2, fib_dict)
    fib_dict[n] = ans
    return ans
