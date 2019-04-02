def file_length(file_name):
    '''Return the number of lines in a file. Returns 0 if it doesn't exist.'''

    try:
        with open(file_name) as file_to_check:
            for index, _ in enumerate(file_to_check):
                pass
            return index + 1  # Will return UnboundLocalError if file is empty
    except (FileNotFoundError, UnboundLocalError):
        return 0
