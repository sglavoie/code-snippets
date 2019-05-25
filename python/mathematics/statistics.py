def find_average():
    """Print the average of the numbers in a list from 0 up to given input."""
    for i in range(int(input())):
        array = list(map(int, input().split()))
        print(round(sum(array) / (len(array) - 1)), end=" ")
