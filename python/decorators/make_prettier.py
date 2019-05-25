def better_separation(the_function):
    """Decorator used to print separators around `the_function`."""

    def print_separator(*args, **kwargs):
        """Surrounds `the_function` with a separator and add a new line."""
        separator = SEP * TERMINAL_WIDTH
        print(separator)
        the_function(*args, **kwargs)
        print(separator, "\n")

    return print_separator
