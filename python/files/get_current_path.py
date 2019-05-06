from pathlib import Path


def get_current_path():
    """Returns the current working directory relative to where this script is
    being executed."""

    return Path(__file__).parents[0]
