"""
This module provides a function to determine the size of a t-shirt 
based on the given measurement in centimeters.
"""
def size(cms):
    """
    Determine the size based on the given measurement in centimeters.

    Args:
        cms (int): The measurement in centimeters.

    Returns:
        str: The size ('S', 'M', or 'L').
    """
    if cms < 38:
        return 'S'
    if 38 <= cms < 42:
        return 'M'
    return 'L'
