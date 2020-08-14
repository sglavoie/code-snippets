import string


def generate_alpha_dict():
    """Return a dictionary mapping a key `letter` with a value
    `number`."""
    return {k: v + 1 for v, k in enumerate(string.ascii_uppercase)}
