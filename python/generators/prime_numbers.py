def gen_primes():
    '''Generator of prime numbers.'''
    list_primes = [2, 3]
    candidate = 4
    yield list_primes[0]
    yield list_primes[1]
    while True:
        prime_tester = 0
        for number in list_primes:
            if candidate % number == 0:
                break
            else:
                prime_tester += 1
        if prime_tester == len(list_primes):
            list_primes.append(candidate)
            yield candidate
            candidate += 1
        else:
            candidate += 1
