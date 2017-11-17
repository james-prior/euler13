"""
euler_13.py - 
"""

def first_ten_digits(x):
    """
    Extract the first ten digits from input.
    :param x: input (too long) number
    :return: first 10 digits of the number
    """
    nbr_string = str(x)
    first_digits = int(nbr_string[:10])
    return first_digits
