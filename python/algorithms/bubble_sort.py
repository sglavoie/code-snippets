def bubble_sort(array_list):
    """Returns the number of passes made through the list and the total number
       of swaps made using "Bubble Sort" sorting algorithm."""
    swap_array = array_list[:]
    pass_count = 0
    swap_count = 0

    swaps_in_pass = True
    while swaps_in_pass:  # while change is made in list
        current_swaps = 0  # will check if swaps are made in current for loop
        pass_count += 1  # we must loop through array, so that's a forced pass
        for index in range(len(array_list) - 1):
            first_value = swap_array[index]
            second_value = swap_array[index + 1]
            if first_value > second_value:
                swap_array[index] = second_value
                swap_array[index + 1] = first_value
                current_swaps += 1
        if current_swaps == 0:  # No swaps made from first to last element
            # pass_count and swap_count are already updated by this point
            break
        else:
            # adds number of swaps for current pass to total number of swaps
            swap_count += current_swaps

    return pass_count, swap_count


def bubble_sort(array_list):
    """Returns a list of indexes of sorted values in 'array_list'.
       For example:
       Initial array: 50 98 17 79   Sorted array: 17 50 79 98
       17 was at 3-rd place initially, 50 was at 1-st place initially
       79 was at 4-th place initially, 98 was at 2-nd place initially
       Result: 3 1 4 2"""

    swap_array = array_list[:]

    while True:  # while change is made in list
        current_swaps = 0
        for index in range(len(array_list) - 1):
            first_value = swap_array[index]
            second_value = swap_array[index + 1]
            if first_value > second_value:
                swap_array[index] = second_value
                swap_array[index + 1] = first_value
                current_swaps += 1
        if current_swaps == 0:  # No swaps made from first to last element
            # pass_count and swap_count are already updated by this point
            break

    return swap_array


def bubble_sort(n, lst):
    """`lst` (list) of `n` elements. Returns the number of swaps
    necessary to sort, the first element and the last one."""
    sorted_lst = False
    swaps_total = 0
    while not sorted_lst:
        swaps_current = 0
        for index in range(n - 1):
            if lst[index] > lst[index + 1]:
                lst[index + 1], lst[index] = lst[index], lst[index + 1]
                swaps_current += 1

        swaps_total += swaps_current

        if swaps_current == 0:
            sorted_lst = True

    return swaps_total, lst[0], lst[-1]
