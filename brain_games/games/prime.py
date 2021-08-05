#!/usr/bin/env python3

import random


def check_prime():
    expression = random.randint(1, 100)
    composite_dividers = list(range(2, expression))
    if expression == 1:
        return ("no", expression)
    for i in composite_dividers:
        if expression % i == 0:
            return ("no", expression)
    return ("yes", expression)
