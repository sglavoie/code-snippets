"""Compute the result of a^b (mod k) by using the exponentiation technique.

The goal here is not efficiency, even though the program is actually pretty
fast: the algorithm is applied manually for demonstration purposes.

Testing on a modest Intel Core i5, having `a` and `b` each set to a random
number containing 2,000 digits and `k` set to a modulo of a number containing
20 digits, results are printed in about 3.3 seconds.

If efficiency matters, this code can be reduced quite substantially as
demonstrated here:

https://math.stackexchange.com/questions/195634/
how-do-you-calculate-the-modulo-of-a-high-raised-number#answer-453108

It would result in the following function using bitwise operations:

def mod_pow(base, exp, mod):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = res * base % mod
        exp = exp >> 1
        base = base**2 % mod
    return res
"""


def binary_remainders(num_b):
    """Take `b` and return the binary equivalent in a list of remainders."""
    remainders = []
    quotient = num_b
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
            powers.append(2 ** index)

    return powers


def compute_intermediate_congruences(num_a, num_k, powers=None):
    """Compute all necessary intermediate results of congruence in `mod k` for
    powers of 2 in `powers` to form the number `b`."""
    if powers is None:
        return None

    go_up_to = max(powers)

    intermediate_results = {1: num_a}  # Build dictionary to store all results
    start_value = 2  # First power of two to calculate congruence
    congruence = num_a
    while start_value <= go_up_to:
        # value to use for next power of 2
        congruence = congruence ** 2 % num_k
        intermediate_results[start_value] = congruence
        start_value *= 2

    return intermediate_results


def compute_final_congruence(num_k, powers=None, intermediate_results=None):
    """Take all relevant values from `intermediate_results` matching powers in
    `powers`, multiply them together and calculate this number `mod k` to get
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
    for result in congruent_results:
        total = result * total  # Multiply all results together

    return total % num_k  # final congruence we are looking for


def compute_congruence(num_a, num_b, num_k):
    """Return `c`, the result of `a^b (mod k)`."""
    num_a = num_a % num_k  # Make sure `a` is smaller than `k`

    # Reduce `b` to list of remainders in binary
    remainders = binary_remainders(num_b)

    # Build a list of the powers of 2 forming `b`
    powers = powers_of_two(remainders)

    # Build a list of necessary intermediate results to reach
    # the value of `b` from powers of 2: finds congruence for
    # smaller powers of 2 and store them in a list.
    intermediate_results = compute_intermediate_congruences(num_a, num_k, powers)

    # Multiply all relevant intermediate results `mod k` to get the final
    # congruence of `a^b (mod k)`.
    return compute_final_congruence(num_k, powers, intermediate_results)


if __name__ == "__main__":
    print("We will calculate a^b (mod k). Enter only integers.")
    NUM_A = int(input("Provide `a`: "))
    NUM_B = int(input("Provide `b`: "))
    NUM_K = int(input("Provide `k`: "))

    FINAL_RESULT = compute_congruence(NUM_A, NUM_B, NUM_K)
    print(FINAL_RESULT)
