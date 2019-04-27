"""Compute the result of a^b (mod p) by using the exponentiation technique.

The goal here is not efficiency, even though the program is actually pretty
fast: the algorithm is applied manually for demonstration purposes.

Testing on a modest Intel Core i5, having `a` and `b` each set to a random
number containing 2,000 digits and `p` set to a modulo of a number containing
20 digits, results are printed in about 3.3 seconds."""

def binary_remainders(b):
    """Take `b` and return the binary equivalent in a list of remainders."""
    remainders = []
    quotient = b
    while True:
        prev_quotient = quotient
        quotient //= 2
        remainder = prev_quotient % 2
        remainders.append(remainder)

        if quotient == 0:
            break

    return remainders


def powers_of_two(remainders=None):
    """Return a list of the value of powers of two that form the
    exponent`b`."""
    if remainders is None:
        return None

    powers = []
    for index, remainder in enumerate(remainders):
        if remainder == 1:
            powers.append(2**index)

    return powers


def compute_intermediate_congruences(a, p, powers=None):
    """Compute all necessary intermediate results of congruence in `mod p` for 
    powers of 2 in `powers` to form the number `b`."""
    if powers is None:
        return None

    go_up_to = max(powers)

    intermediate_results = {1: a}  # Build dictionary to store all results
    start_value = 2  # First power of two to calculate congruence
    congruence = a
    while start_value <= go_up_to:
        # value to use for next power of 2
        congruence = congruence ** 2 % p
        intermediate_results[start_value] = congruence
        start_value *= 2

    return intermediate_results


def compute_final_congruence(p, powers=None, intermediate_results=None):
    """Take all relevant values from `intermediate_results` matching powers in
    `powers`, multiply them together and calculate this number `mod p` to get
    the final result."""
    if intermediate_results is None or powers is None:
        return None

    # store all required values from `intermediate_results`
    congruent_results = []
    for power in powers:
        for key, value in intermediate_results.items():
            if key == power:
                congruent_results.append(value)

    total = 1
    for result in congruent_results:  # Multiply all results together
         total = result * total  
    
    return total % p  # final congruence we are looking for


def compute_congruence(a, b, p):
    """Return `c`, the result of `a^b (mod p)`."""
    a = a % p  # Make sure `a` is smaller than `p`

    # Reduce `b` to list of remainders in binary
    remainders = binary_remainders(b)
    
    # Build a list of the powers of 2 forming `b`
    powers = powers_of_two(remainders)

    # Build a list of necessary intermediate results to reach
    # the value of `b` from powers of 2: finds congruence for
    # smaller powers of 2 and store them in a list.
    intermediate_results = compute_intermediate_congruences(a, p, powers)

    # Multiply all relevant intermediate results `mod p` to get the final
    # congruence of `a^b (mod p)`.
    return compute_final_congruence(p, powers, intermediate_results)


if __name__ == '__main__':
    print("We will calculate a^b (mod p). Enter only integers.")
    a = int(input("Provide `a`: "))
    b = int(input("Provide `b`: "))
    p = int(input("Provide `p`: "))

    result = compute_congruence(a, b, p)
    print(result)