#! /usr/bin/python3
# -*- coding: utf-8 -*-
from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        if discriminant == 0:
            return root1, None
        else:
            return root1, root2
    else:
        return None, None
