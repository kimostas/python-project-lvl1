#!/usr/bin/env python


import random


def is_even():
    number = random.randint(1, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (answer, number)
