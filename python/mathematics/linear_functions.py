def find_slope(int_a, int_b, int_c, int_d):
    '''Returns the slope of a linear function.'''
    return int((int_d - int_b) / (int_c - int_a))


def find_intercept(int_a, int_b, int_m):
    '''Returns the intercept of a linear function.'''
    return int(int_b - (int_m * int_a))
