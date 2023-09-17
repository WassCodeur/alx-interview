#!/usr/bin/env python3


def pascal_triangle(n):
    father = [[]]
    child = []
    if n <= 0:
        return []
    else:
        for i in range(n):
            father[i] = child
            
