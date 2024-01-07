""" https://adventofcode.com/2023/day/4
"""

import re

def get_winnumbers(line: str) -> list:
    """
    Extracts the winning numbers from a given line.

    Args:
        line (str): The input line containing the winning numbers.

    Returns:
        list: A list of winning numbers extracted from the line.
    """
    match = re.search(r'Card\s*\d+:\s*((?:\d+\s*)+)\|', line)
    numbers = []
    if match:
        numbers = match.group(1).split()
    return numbers

def get_rightnumbers(line: str) -> list:
    """
    Extracts a list of numbers from a given string.

    Args:
        line (str): The input string.

    Returns:
        list: A list of numbers extracted from the input string.
    """
    match = re.search(r'\|\s*((?:\d+\s*)+)', line)
    numbers = []
    if match:
        numbers = match.group(1).split()
    return numbers

def calculate_cardpoints(line: str) -> int:
    """
    Calculate the points for a given line of card numbers.

    Args:
        line (str): The line of card numbers.

    Returns:
        int: The calculated points.

    """
    points = 0
    matches = []
    win_numbers = get_winnumbers(line)
    right_numbers = get_rightnumbers(line)
    for number in right_numbers:
        if number in win_numbers:
            matches.append(number)
    if matches:
        points = 2 ** (len(matches) - 1)
    return points

def main(input: str) -> int:
    with open(input) as f:
        sum = 0
        lines = f.readlines()
        for line in lines:
            sum += calculate_cardpoints(line)
    return sum


if __name__ == "__main__":
    print(main("input.txt"))
            
