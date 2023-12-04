#!/usr/bin/python3
"""interview prep"""


def island_perimeter(grid):
    """island perimeter

    Arguments
    ---------
    grid: list of list

    Return
    ------
    None
    """
    heigh = 1
    width = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if (i + 1) < (len(grid) - 1):
                    if grid[i + 1][j]:
                        heigh += 1

                    if (j + 1) < (len(grid[i])):
                        width += 1

    per = (heigh + width) * 2

    return (per)
