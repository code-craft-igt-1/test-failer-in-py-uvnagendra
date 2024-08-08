"""
This module provides functionality to determine the major and minor 
color based on a given pair number.
"""

MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_map():
    """
    Generate a color map for the major and minor colors.

    Returns:
        tuple: A tuple containing the color map list and the total number of color combinations.
    """
    color_map = []
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    color_combinations = len(MAJOR_COLORS) * len(MINOR_COLORS)
    return color_map, color_combinations

def get_color_from_pair_number(pair_number):
    """
    Get the major and minor color from the pair number.

    Args:
        pair_number (int): The pair number.

    Returns:
        tuple: A tuple containing the major and minor color.

    Raises:
        Exception: If the major or minor index is out of range.
    """
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MAJOR_COLORS):
        raise Exception('Minor index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
