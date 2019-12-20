def file_length(file_name):
    """Return the number of lines in a file. Returns 0 if it doesn't exist."""

    try:
        with open(file_name) as file_to_check:
            total = 0
            for index, _ in enumerate(file_to_check):
                total = index + 1
            return total
    except FileNotFoundError:
        return 0


if __name__ == "__main__":
    print(file_length("rename.py"))  # 15
