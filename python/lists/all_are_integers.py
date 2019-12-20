def is_all_int(list_int: list) -> bool:
    all_positive = [x >= 0 for x in list_int]
    return all(all_positive)
