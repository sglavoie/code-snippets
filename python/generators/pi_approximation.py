def odd_numbers_gen(n=1):
    while True:
        yield n
        n += 2


def pi_approximation():
    approximation = 0
    odds_sequence = odd_numbers_gen()
    while True:
        approximation += 4 / next(odds_sequence)
        yield approximation
        approximation -= 4 / next(odds_sequence)
        yield approximation
