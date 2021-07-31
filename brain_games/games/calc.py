#!/usr/bin/env python
import random
import operator


def check_calc():
        numb_1 = random.randint(1, 50)
        numb_2 = random.randint(1, 50)
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }
        op = random.choice(list(operators.keys()))
        answer = operators[op](numb_1, numb_2)
        expression = f"{numb_1} {op} {numb_2}"
        return (str(answer), expression)