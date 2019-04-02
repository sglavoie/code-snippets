def odd_numbers_gen():
    current = 1
    while True:
        yield current
        current += 2
