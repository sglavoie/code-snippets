import string


def generate_alpha_dict():
    """Return a dictionary mapping a key `letter` with a value
    `number`."""
    alpha_dict = {k: v+1 for v, k in enumerate(string.ascii_uppercase)}
    return alpha_dict
