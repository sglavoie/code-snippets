from collections.abc import Container


def round_float(x, decimals=2):
    return round(x, decimals)


def round_floats_recursively(pydict, func=round_float):
    if isinstance(pydict, dict):
        return type(pydict)(
            (key, round_floats_recursively(value, func))
            for key, value in pydict.items()
        )
    if isinstance(pydict, Container):
        return type(pydict)(
            round_floats_recursively(value, func) for value in pydict
        )
    if isinstance(pydict, float):
        return func(pydict)  # only round floats
    return pydict
