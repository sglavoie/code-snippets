def equalize_array(arr: list) -> int:
    """Count the minimum number of deletions that must be made in an array to
       end up with an array that contains only one element that can repeat
       itself. Examples: [1, 1, 1], [2, 2], [3, 3, 3, 3], etc.
       Returns integer."""
    arr2 = arr[:]
    arr_dict = dict_count(arr)
    max_count = max(arr_dict.values())
    for key, value in arr_dict.items():
        if value == max_count:
            chosen_key = key
            break
    deletion_count = 0
    for value in arr:
        if value != chosen_key:
            arr2.remove(value)
            deletion_count += 1
    return deletion_count
