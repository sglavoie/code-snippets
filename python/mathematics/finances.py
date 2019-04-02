def waiting_time(starting_amount, required_amount, interest_rate):
    """Returns the waiting time to get to `required_amount` from
    `starting_amount` at `interest_rate` (in percent) as a integer."""
    accumulated = starting_amount  # amount being accumulated after each year
    years_passed = 0  # number of years that have passed to get to `accumulated`
    interest_factor = interest_rate / 100 + 1
    while accumulated < required_amount:
        accumulated = accumulated * interest_factor
        accumulated = math.floor(accumulated * 100) / 100
        years_passed += 1
    return years_passed
