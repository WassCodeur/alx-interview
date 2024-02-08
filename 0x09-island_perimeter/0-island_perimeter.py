#!/usr/bin/python3
"""island perimeter"""


def island_perimeter(grid):
    """island perimeter

    Arrguments
    ----------
    grid: list of list of int

    Return
    ------
    perimeter: int
    """
    heigh = len(grid)
    perimeter = 0
    for h in range(heigh):
        width = len(grid[h])
        for w in range(width):
            prev_h = h - 1
            prev_w = w - 1
            if grid[h][w] == 1:
                perimeter += 4
                if prev_h >= 0:
                    if grid[prev_h][w] == 1:
                        perimeter -= 2
                if prev_w >= 0:
                    if grid[h][prev_w] == 1:
                        perimeter -= 2
    return perimeter
