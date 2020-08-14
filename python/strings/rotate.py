def rotate_string(index_rotation, string_to_rotate):
    """Return a string, rotating it by `index_rotation`."""
    beginning = string_to_rotate[index_rotation:]
    end = string_to_rotate[:index_rotation]
    return beginning + end
